from django.db.models import (
    Model,
    IntegerField,
    FloatField,
    BooleanField,
    GenericIPAddressField,
    CharField,
)


class LocationModel(Model):
    geoname_id = IntegerField()
    capital = CharField(max_length=100)
    country_flag = CharField(max_length=500)
    country_flag_emoji = CharField(max_length=10)
    country_flag_emoji_unicode = CharField(max_length=70)
    calling_code = CharField(max_length=10)
    is_eu = BooleanField()

    def __repr__(self):
        return 'aa'


class GeolocationModel(Model):
    ip = GenericIPAddressField()
    hostname = GenericIPAddressField(blank=True, null=True)
    type = CharField(max_length=4)
    continent_code = CharField(max_length=8)
    continent_name = CharField(max_length=100)
    country_code = CharField(max_length=8)
    country_name = CharField(max_length=100)
    region_code = CharField(max_length=8)
    region_name = CharField(max_length=100)
    city = CharField(max_length=100)
    zip = CharField(max_length=10)
    latitude = FloatField()
    longitude = FloatField()
    location = LocationModel()

    def __repr__(self):
        return 'bb'

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
