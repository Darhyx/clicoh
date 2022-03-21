from collections import defaultdict
from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
#
from . import viewsets

router =  DefaultRouter()

router.register(r'order', 
                viewsets.OrderViewSet, 
                basename= 'order')
router.register(r'orderdetail', 
                viewsets.OrderdetailViewSet, 
                basename= 'orderdetail')
router.register(r'register', 
                viewsets.RegisterOrderDetailViewset, 
                basename= 'report')
urlpatterns = router.urls