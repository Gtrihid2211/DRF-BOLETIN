from django.contrib.auth.models import Group, User
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import permissions, viewsets, filters
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from vehiculos.filters import VehiculoFilter
from vehiculos.models import Vehiculo, Marca
from vehiculos.permissions import IsAuthenticated
from vehiculos.serializers import GroupSerializer, UserSerializer, VehiculoSerializer, MarcaSerializer
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_fields = ['modelo', 'color', 'marca__nombre']
    ordering_fields = ['fecha_fabricacion']
    ordering = ['fecha_fabricacion']  # Default ordering
    filterset_class = VehiculoFilter


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]


