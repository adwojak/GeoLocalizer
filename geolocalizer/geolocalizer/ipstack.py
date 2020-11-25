from dotenv import load_dotenv
from os import getenv, path
from requests import get as rget
from typing import Tuple
from geolocalizer.settings import BASE_DIR
from geolocalizer.constants import APP_NAME, ENV_FILE_NAME, IPSTACK_API_KEY, IPSTACK_API_URL
from geolocalizer.libs.validators import validate_address

env_path = path.join(BASE_DIR, APP_NAME, ENV_FILE_NAME)
load_dotenv(dotenv_path=env_path)


access_key = getenv(IPSTACK_API_KEY)


def validate_addresses(func):
    def validate(*args):
        for address in args:
            if not validate_address(address):
                raise NotImplementedError
        return func(*args)
    return validate


def _get_url(addresses_list: Tuple[str]) -> str:
    joined_addresses_list = ','.join(addresses_list)
    return f'{IPSTACK_API_URL}{joined_addresses_list}?access_key={access_key}'


@validate_addresses
def fetch_ipstack(*addresses_list: str) -> dict:
    return rget(_get_url(addresses_list)).json()
#
# a = {
#     'ip': '2607:f8b0:4005:804::2004',
#     'type': 'ipv6',
#     'continent_code': 'NA',
#     'continent_name':'North America',
#     'country_code': 'US',
#     'country_name': 'United States',
#     'region_code': 'CA',
#     'region_name': 'California',
#     'city': 'Mountain View',
#     'zip': '94043',
#     'latitude': 37.38801956176758,
#     'longitude': -122.07431030273438,
#     'location': {
#         'geoname_id': 5375480,
#         'capital': 'Washington D.C.',
#         'languages': [
#             {
#                 'code': 'en',
#                 'name': 'English',
#                 'native': 'English'
#             }
#         ],
#         'country_flag': 'http://assets.ipstack.com/flags/us.svg',
#         'country_flag_emoji': '🇺🇸',
#         'country_flag_emoji_unicode': 'U+1F1FA U+1F1F8',
#         'calling_code': '1',
#         'is_eu': False
#     }
# }
#
# loc = {
#     'geoname_id': 5375480,
#     'capital': 'asdzxsc',
#     'languages': [
#         {
#             'code': 'lolo',
#             'name': 'English',
#             'native': 'English'
#         },
#         {
#             'code': 'dupa',
#             'name': 'kaska',
#             'native': 'kakqewa'
#         }
#     ],
#     'country_flag': 'http://assets.ipstack.com/flags/us.svg',
#     'country_flag_emoji': '🇺🇸',
#     'country_flag_emoji_unicode': 'U+1F1FA U+1F1F8',
#     'calling_code': '1',
#     'is_eu': False
# }
# from geolocalizer.geolocalizer.serializers import LocationSerializer
