from argparse import ArgumentParser
from json import dumps

from . import OktaToken


def main() -> str:
    """
    Used as an entrypoint for terminal script. Creates the arguments from OktaToken from cmdline args,
    fetches a token, and logs it to stdout before returning it.
    """
    from sys import stdout
    from logging import basicConfig

    basicConfig(stream=stdout, format="%(message)s")

    epilog = """
    This script builds off of the dirty quick way to get a token from your browser stated here:
    https://developer.okta.com/docs/guides/implement-oauth-for-okta/main/#get-an-access-token-and-make-a-request .

    This is done by opening a browser window that navigates to the auth server with localhost as the redirect_uri. There
    is an http server that is spun up for just long enough to handle the redirect request and get the id_token from the
    query parameters that are sent via window.hash (I suppose OKTA does this so that it can't be sent to the server itself).

    Note that when using this tool your OKTA JWT will:
      * Be stored in ~/.okta_token (700 file permissions) unless --no-cache is specified
      * Be visible in the url bar of your browser for a few seconds
      * Be visible on the page after all of the redirects for 3 seconds before being redirected to a final page in your browser

    Your OKTA application MUST have "http://localhost:8888" configured as one of the allowed redirect uri's for this tool to work.
  """
    parser = ArgumentParser(epilog=epilog)

    parser.add_argument(
        "-i",
        "--issuer",
        required=True,
        help="The auth server url. This should be only the domain and protocol. eg: https://mydomain.okta.com",
    )
    parser.add_argument(
        "-c", "--client-id", required=True, help="The client id to get a token for"
    )
    parser.add_argument(
        "-s",
        "--scopes",
        help="Comma delimited list of scopes to request",
        default="openid",
    )
    parser.add_argument(
        "-t", "--token-type", help="The type of token to request", default="id_token"
    )
    parser.add_argument("--no-cache", help="Don't cache the token", action="store_true")
    parser.add_argument("-S", "--keychain-service", help="Service name to use when caching tokens to the OS keychain. Defaults to the issuer", type=str, default="")
    parser.add_argument("-u", "--keychain-username", help="Username to use when caching tokens to the OS keychain. Defaults to the client ID", type=str, default="")
    parser.add_argument("-r", "--final-redirect", help="This is where the browser will be redirected to at the end of the auth flow", type=str, default="https://github.com")
    parser.add_argument("-I", "--info", help="Print info about the token", action="store_true")
    args = parser.parse_args()
    args.scopes = args.scopes.split(",")

    fetcher = OktaToken(
        issuer=args.issuer,
        client_id=args.client_id,
        scopes=args.scopes,
        token_type=args.token_type,
        use_keychain=not args.no_cache,
        final_redirect=args.final_redirect,
        keychain_service=args.keychain_service,
        keychain_username=args.keychain_username
    )

    if args.info:
        print(dumps(fetcher.token_info, indent=2))

    return fetcher.token
