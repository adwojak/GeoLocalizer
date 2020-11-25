from rest_framework.serializers import HyperlinkedModelSerializer
from geolocalizer.geolocalizer.models import GeolocationModel, LocationModel, LanguageModel


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
        try:
            return self.Meta.model.objects.get_or_create(**validated_data)[0]
        except self.Meta.model.MultipleObjectsReturned:
            return self.Meta.model.objects.filter(**validated_data).first()
