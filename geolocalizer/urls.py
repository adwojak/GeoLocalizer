from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from geolocalizer.geolocalizer import views


router = DefaultRouter()
router.register(r'languages', views.LanguageViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'geolocations', views.GeolocationViewSet)
router.register(r'fetch-address', views.AddAddressViewSet, basename='fetch-address')
router.register(r'register', views.RegisterViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
