from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from geolocalizer.geolocalizer.models import LocationModel, LanguageModel, GeolocationModel
from geolocalizer.geolocalizer.serializers import(
    LocationSerializer,
    LanguageSerializer,
    GeolocationSerializer,
    AddressSerializer,
)


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
        # Send request to ipstack
        return Response(serializer.data)
