from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from geolocalizer.geolocalizer.models import LocationModel, LanguageModel, GeolocationModel
from geolocalizer.geolocalizer.serializers import(
    LocationSerializer,
    LanguageSerializer,
    GeolocationSerializer,
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


class AddAddress(ViewSet):

    def list(self, request):
        # Display shorter version of addresses
        return Response({"a": "q"})

    def create(self, request):
        serializer = AddressSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        address = serializer.validated_data['address']
        ipstack_data = fetch_ipstack(address, omit_validation=True)
        return Response(ipstack_data)
