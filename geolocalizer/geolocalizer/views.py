from typing import Any
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from geolocalizer.libs.errors import DATA_NOT_FOUND
from geolocalizer.libs.exceptions import IpstackDataNotFoundError
from geolocalizer.libs.response import SuccessResponse
from geolocalizer.geolocalizer.models import LocationModel, LanguageModel, GeolocationModel
from geolocalizer.geolocalizer.serializers import (
    LocationSerializer,
    LanguageSerializer,
    GeolocationSerializer,
    GeolocationDescriptionSerializer,
    AddressSerializer,
    RegisterSerializer,
)
from geolocalizer.geolocalizer.ipstack import fetch_ipstack


class DeleteUserView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.user.delete()
        return SuccessResponse('User deleted', status=HTTP_204_NO_CONTENT)


class RegisterViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class GeolocationViewSet(ModelViewSet):
    queryset = GeolocationModel.objects.all()
    serializer_class = GeolocationSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer(self, *args: Any, **kwargs: Any):
        method = self.request.method
        serializer_instance = super(GeolocationViewSet, self).get_serializer(*args, **kwargs)
        if method in ['PUT', 'PATCH']:
            serializer_instance.partial = True
        return serializer_instance

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return SuccessResponse('Geolocation deleted', status=HTTP_204_NO_CONTENT)


class LocationViewSet(ReadOnlyModelViewSet, UpdateModelMixin):
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args: Any, **kwargs: Any):
        method = self.request.method
        serializer_instance = super(LocationViewSet, self).get_serializer(*args, **kwargs)
        if method in ['PUT', 'PATCH']:
            serializer_instance.partial = True
        return serializer_instance


class LanguageViewSet(ReadOnlyModelViewSet, UpdateModelMixin):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAuthenticated,)


class AddAddressViewSet(GenericViewSet, ListModelMixin):
    queryset = GeolocationModel.objects.all()
    serializer_class = GeolocationDescriptionSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request: Request) -> Response:
        serializer = AddressSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        address = serializer.validated_data['address']
        ipstack_data = fetch_ipstack(address, omit_validation=True)
        if ipstack_data['continent_name'] is None:
            raise IpstackDataNotFoundError(DATA_NOT_FOUND.format(address))
        geolocation_model = GeolocationSerializer().create(ipstack_data)
        geolocation_data = GeolocationSerializer(geolocation_model, context={'request': request}).data
        return Response(geolocation_data, status=HTTP_201_CREATED)
