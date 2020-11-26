from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from geolocalizer.libs.renderers import BrowsableAPIRendererWithOtherInputContent
from geolocalizer.geolocalizer.models import LocationModel, LanguageModel, GeolocationModel
from geolocalizer.geolocalizer.serializers import (
    LocationSerializer,
    LanguageSerializer,
    GeolocationSerializer,
    GeolocationDescriptionSerializer,
    AddressSerializer,
)
from geolocalizer.geolocalizer.ipstack import fetch_ipstack


class GeolocationViewSet(ModelViewSet):
    queryset = GeolocationModel.objects.all()
    serializer_class = GeolocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer


class LanguageViewSet(ModelViewSet):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer


class AddAddress(GenericViewSet, ListModelMixin):
    queryset = GeolocationModel.objects.all()
    serializer_class = GeolocationDescriptionSerializer
    input_serializer_class = (AddressSerializer, ['POST'])
    renderer_classes = (JSONRenderer, BrowsableAPIRendererWithOtherInputContent)

    def create(self, request):
        serializer = AddressSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        address = serializer.validated_data['address']
        ipstack_data = fetch_ipstack(address, omit_validation=True)
        geolocation_model = GeolocationSerializer().create(ipstack_data)
        geolocation_data = GeolocationSerializer(geolocation_model, context={'request': request}).data
        return Response(geolocation_data)

# {"address":"www.google.com"}
# url, continent_name, country_name, region_name, city, ip