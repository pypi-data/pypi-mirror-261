#!/usr/bin/env python3
from urllib.parse import urlparse, parse_qs, urlencode
from time import sleep, time
from requests import get
from requests.exceptions import ConnectionError
from webbrowser import open_new_tab
from threading import Thread
from jwt import decode
from typing import List

import http.server

import keyring


class Handler(http.server.SimpleHTTPRequestHandler):
    """
    Handles requests to the local web server.
    * The first request to the server will be to /ready, which signals that we are ready to browse to the auth server endpoint and the redirect will work
    * The second request is to localhost:8888/, which will get the has from the window.location and redirect back to the server with the correct parameters
    * The third request is to /gettoken, which will parse the id_token from the GET parameters and return it
    """

    token: str = None
    token_url: str = None
    final_redirect: str = None

    @property
    def redirect_html(self):
        return """
        <script>
            hash = window.location.hash.replace(/^#/, "?")
            console.log(hash)
            url = "http://localhost:8888/gettoken" + hash
            console.log(url)
                window.location.href = url
        </script>
        """.encode()

    @property
    def auth_failed_html(self):
        return """
        <div style="text-align:center">
            <h1>401 NOT AUTHORIZED</h1>
            <h2>____________________________________</h2>
            <h2>Could not log into OKTA</h2>
        </div>
        """.encode()

    @property
    def auth_success_html(self):
        return f"""
          <script>
              window.location.href = '{self.final_redirect}'
          </script>
        """.encode()

    # We don't really need any http logging for this
    def log_message(self, _, *__) -> None:
        pass

    def do_GET(self):
        """
        Our request handler
        """

        def send_headers(code, res) -> None:
            """
            Sets response headers
            """
            self.send_response(code, res)
            self.send_header("Content-type", "html")
            self.end_headers()

        req = urlparse(self.path)
        qry = req.query
        req_path = req.path

        if req_path == "/ready":
            send_headers(200, "OK")
            self.wfile.write("ready".encode())

        elif req_path == "/gettoken":
            token = parse_qs(qry).get("id_token") or parse_qs(qry).get("access_token")
            if token is None:
                send_headers(401, "NOT AUTHORIZED")
                self.wfile.write(self.auth_failed_html)
                exit(1)
            else:
                Handler.token = token[0]

                send_headers(200, "OK")
                self.wfile.write(self.auth_success_html)

        # This handles any 'other' requests, such as /favicon.ico
        elif req_path == "/":
            send_headers(200, "Redirecting")
            self.wfile.write(self.redirect_html)
        else:
            send_headers(404, "NOT FOUND")


def open_link():
    """
    Handles the browser iteraction.
      * Make requests to /ready until we get a 200 and "ready" in the body
      * Open a browser to the auth server url and follow the redirects
      * The server will get the JWT from the dance it does with redirects
    """

    while True:
        try:
            res = get("http://localhost:8888/ready")
        except ConnectionError:
            sleep(1)
            continue
        if res.content.decode() == "ready":
            open_new_tab(Handler.token_url)
            return
        sleep(1)


class OktaToken:
    """
    Starts an http server that opens a browser window for logging into OKTA (if not already) and retrieves an
    id_token by using a local server as the redirect URI in the OKTA auth url parameters.
    """

    def __init__(
        self,
        issuer: str,
        client_id: str,
        final_redirect: str,
        scopes: List[str] = ["openid"],
        token_type: str = "id_token",
        use_keychain: bool = True,
        keychain_username: str = "",
        keychain_service: str = "",
    ) -> None:
        self.issuer = issuer
        self.client_id = client_id
        self.scopes = scopes
        self.__token = None

        self.token_type = token_type
        self.use_keychain = use_keychain
        self.keychain_service = keychain_service or self.issuer
        self.keychain_username = keychain_username or self.client_id

        self.token_url = self.make_tokenurl()

        # Kinda hacky, but hey, this whole thing kinda is.....
        Handler.token_url = self.token_url
        Handler.final_redirect = final_redirect
        self.get_token()

    @property
    def token(self) -> str:
        """
        Returns the stored OKTA token. A new token will be generated if:
          * self.use_keychain == False
          * A token has not been previously cached
          * There is a cached token, but it has expired
        """
        if self.__token is None or not self.is_valid:
            self.get_new_token()
        return self.__token

    def make_tokenurl(self):
        """
        Builds the url sent to the browser for logging in. Taken from:
        https://developer.okta.com/docs/guides/implement-oauth-for-okta/main/#get-an-access-token-and-make-a-request
        """
        params = {
            "client_id": self.client_id,
            "response_type": self.token_type,
            "nonce": 1234,
            "scope": " ".join(self.scopes),
            "state": "test",
            "redirect_uri": "http://localhost:8888",
        }

        # The replace method is there because urllib does not correctly encode spaces when passing a dict.
        # The other option is building a string from the dict and passing it to urlencode which, IMO, is just as ugly.
        # We know what the parameters are what they will contain, so this shouldn't be an issue.
        param_str = urlencode(params).replace("+", "%20")
        url = f"{self.issuer}/v1/authorize?{param_str}"
        return url

    def is_valid(self) -> bool:
        """
        Tests if we can decode the JWT and if it has not expired.
        We DO NOT validate the signature on the token.
        """
        try:
            data = decode(
                self.token, algorithms="RS256", options={"verify_signature": False}
            )
        except Exception as e:
            print(f"Could not validate token: {e}")
            exit(1)

        return not data.get("exp", 0) < time()

    def get_from_keychain(self):
        if not self.use_keychain:
            return
        else:
            return keyring.get_password(self.keychain_service, self.keychain_username)

    def cache_token(self):
        keyring.set_password(
            self.keychain_service, self.keychain_username, self.__token
        )

    def get_token(self) -> str:
        """
        Update self.token and return it. We will generate a new token if:
          * The token is expired
          * self.token is None and self.use_keychain == False
          * There is an error decoding the token
        """
        if self.use_keychain:
            self.__token = self.get_from_keychain()
        else:
            self.get_new_token()

        if not (self.__token and self.is_valid()):
            self.get_new_token()

        return self.__token

    def get_new_token(self) -> str:
        """
        The big show. This is what we are here for.
          * Start a server to listen for the browser to be redirected to it
          * Make requests to /ready until we get a 200
          * Open a browser to the auth server url and follow the redirects
          * return the JWT from the server class
        """
        s = http.server.HTTPServer(("", 8888), Handler)
        link = Thread(target=open_link, daemon=True)
        link.start()

        while Handler.token is None:
            s.handle_request()

        jwt = Handler.token

        self.__token = jwt

        if self.use_keychain == True:
            self.cache_token()

        return jwt

    @property
    def token_info(self):
        if self.token:
            return decode(
                self.token, algorithms="RS256", options={"verify_signature": False}
            )


def get_user_from_token(token):
    return decode(token, algorithms="RS256", options={"verify_signature": False})["sub"]
