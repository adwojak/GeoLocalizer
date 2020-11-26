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
