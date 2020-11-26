from os import getenv
from requests import get as rget
from geolocalizer.constants import IPSTACK_API_KEY, IPSTACK_API_URL
from geolocalizer.libs.validators import validate_address


def _get_url(address: str) -> str:
    return f'{IPSTACK_API_URL}{address}?access_key={getenv(IPSTACK_API_KEY)}'


def _fetch_ipstack(address: str) -> dict:
    return rget(_get_url(address)).json()


def fetch_ipstack(address: str, omit_validation: bool = False) -> dict:
    if omit_validation:
        return _fetch_ipstack(address)
    else:
        if not validate_address(address):
            raise NotImplementedError
        return _fetch_ipstack(address)
