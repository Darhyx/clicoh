from collections import defaultdict
from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
#
from . import viewsets

router =  DefaultRouter()

router.register(r'product', viewsets.ProductViewSet, basename= 'product')

urlpatterns = router.urls