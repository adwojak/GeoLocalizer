from django.db.models import (
    Model,
    IntegerField,
    FloatField,
    BooleanField,
    GenericIPAddressField,
    CharField,
    ForeignKey,
    ManyToManyField,
    CASCADE,
)


class LanguageModel(Model):
    code = CharField(max_length=10)
    name = CharField(max_length=100)
    native = CharField(max_length=100)


class LocationModel(Model):
    geoname_id = IntegerField()
    capital = CharField(max_length=100)
    languages = ManyToManyField(LanguageModel)
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
    location = ForeignKey(LocationModel, CASCADE)

    def __repr__(self):
        return 'bb'
