from rest_framework.serializers import HyperlinkedModelSerializer, Serializer, CharField, ValidationError
from geolocalizer.geolocalizer.models import GeolocationModel, LocationModel, LanguageModel
from geolocalizer.libs.validators import validate_address
from geolocalizer.libs.errors import ADDRESS_NOT_VALID


class LanguageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LanguageModel
        fields = '__all__'

    def create(self, validated_data):
        try:
            return self.Meta.model.objects.get_or_create(**validated_data)[0]
        except self.Meta.model.MultipleObjectsReturned:
            return self.Meta.model.objects.filter(**validated_data).first()


class LocationSerializer(HyperlinkedModelSerializer):
    languages = LanguageSerializer(many=True)

    class Meta:
        model = LocationModel
        fields = '__all__'

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


class GeolocationSerializer(HyperlinkedModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = GeolocationModel
        fields = '__all__'

    def create(self, validated_data):
        location = validated_data.pop('location')
        try:
            return self.Meta.model.objects.get(**validated_data)
        except self.Meta.model.DoesNotExist:
            location_model = LocationSerializer().create(location)
            return self.Meta.model.objects.create(location=location_model, **validated_data)
        except self.Meta.model.MultipleObjectsReturned:
            return self.Meta.model.objects.filter(**validated_data).first()


class GeolocationDescriptionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = GeolocationModel
        fields = ['url', 'ip', 'city', 'region_name', 'country_name', 'continent_name']


class AddressSerializer(Serializer):
    address = CharField(max_length=300)

    def _validate_bad_address(self, address):
        if not validate_address(address):
            raise ValidationError({'address': ADDRESS_NOT_VALID.format(address)})

    def validate(self, data):
        self._validate_bad_address(dict(data)['address'])
        return data
