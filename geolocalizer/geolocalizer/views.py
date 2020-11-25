from rest_framework.viewsets import ModelViewSet
from geolocalizer.geolocalizer.models import LocationModel, LanguageModel, GeolocationModel
from geolocalizer.geolocalizer.serializers import LocationSerializer, LanguageSerializer, GeolocationSerializer


class GeolocationViewSet(ModelViewSet):
    queryset = GeolocationModel.objects.all()
    serializer_class = GeolocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer


class LanguageViewSet(ModelViewSet):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer
