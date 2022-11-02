from rest_framework import viewsets
from .Serializer import ProductSerializer
from .models import FoodIssine


class ProductViewset(viewsets.ModelViewSet):
    queryset = FoodIssine.objects.all()
    serializer_class = ProductSerializer
