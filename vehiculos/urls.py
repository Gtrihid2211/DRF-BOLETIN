from django.urls import path, include
from .views import VehiculoViewSet, MarcaViewSet, GroupViewSet, UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'marcas', MarcaViewSet)

urlpatterns = [
    # Rutas generadas por el enrutador para vehículos y marcas
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
