from os import getenv
from requests import get as rget, ConnectionError
from geolocalizer.constants import IPSTACK_API_KEY, IPSTACK_API_URL
from geolocalizer.libs.validators import validate_address
from geolocalizer.libs.errors import IPSTACK_UNAVAILAVLE, ADDRESS_NOT_VALID
from geolocalizer.libs.exceptions import BadAddressError


def _get_url(address: str) -> str:
    return f'{IPSTACK_API_URL}{address}?access_key={getenv(IPSTACK_API_KEY)}'


def _fetch_ipstack(address: str) -> dict:
    try:
        return rget(_get_url(address)).json()
    except ConnectionError:
        raise ConnectionError(IPSTACK_UNAVAILAVLE)


def fetch_ipstack(address: str, omit_validation: bool = False) -> dict:
    if omit_validation:
        return _fetch_ipstack(address)
    else:
        if not validate_address(address):
            raise BadAddressError(ADDRESS_NOT_VALID.format(address))
        return _fetch_ipstack(address)
