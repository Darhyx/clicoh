from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product

from .serializers import PorductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    
    serializer_class = PorductSerializer
    permission_classes= (IsAuthenticated,)
    queryset = Product.objects.all()