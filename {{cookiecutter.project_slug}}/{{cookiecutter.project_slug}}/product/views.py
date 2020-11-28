from rest_framework import generics
from rest_framework import viewsets

from . import serializers
from . import models


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
