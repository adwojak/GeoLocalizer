from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# from geolocalizer.geolocalizer.serializers import UserSerializer, GroupSerializer
from geolocalizer.geolocalizer.models import LocationModel, LanguageModel
from geolocalizer.geolocalizer.serializers import LocationSerializer, LanguageSerializer

# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class GroupViewSet(ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [IsAuthenticated]


class LocationViewSet(ModelViewSet):
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer


class LanguageViewSet(ModelViewSet):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer
