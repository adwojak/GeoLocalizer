from django.contrib.auth.models import User, Group
from rest_framework.serializers import HyperlinkedModelSerializer
from geolocalizer.geolocalizer.models import GeolocationModel, LocationModel, LanguageModel


# class UserSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


class GeolocationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = GeolocationModel
        fields = ['url', 'ip', 'hostname', 'type', 'continent_code', 'continent_name', 'country_code', 'country_name',
                  'region_code', 'region_name', 'city', 'zip', 'latitude', 'longitude', 'location', ]


class LanguageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LanguageModel
        fields = ['url', 'code', 'name', 'native', ]

    def create(self, validated_data):
        try:
            return self.Meta.model.objects.get_or_create(**validated_data)[0]
        except self.Meta.model.MultipleObjectsReturned:
            return self.Meta.model.objects.filter(**validated_data).first()


class LocationSerializer(HyperlinkedModelSerializer):
    languages = LanguageSerializer(many=True)

    class Meta:
        model = LocationModel
        fields = ['url', 'geoname_id', 'capital', 'languages', 'country_flag', 'country_flag_emoji',
                  'country_flag_emoji_unicode', 'calling_code', 'is_eu', ]

    def create(self, validated_data):
        languages = validated_data.pop('languages')
        try:
            return self.Meta.model.objects.get(**validated_data)
        except self.Meta.model.DoesNotExist:
            language_models = LanguageSerializer(many=True).create(languages)
            instance = self.Meta.model.objects.create(**validated_data)
            instance.languages.set(language_models)
            return instance
        except self.Meta.model.MultipleObjectsReturned:
            return self.Meta.model.objects.filter(**validated_data).first()
