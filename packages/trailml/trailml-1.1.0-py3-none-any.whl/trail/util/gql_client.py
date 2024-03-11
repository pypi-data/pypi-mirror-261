from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport

from trail.libconfig import libconfig
from trail.util import auth


def build_gql_client():
    transport = AIOHTTPTransport(
        libconfig.gql_endpoint_url,
        headers=auth.build_auth_header(),
    )
    return Client(transport=transport, execute_timeout=30)
