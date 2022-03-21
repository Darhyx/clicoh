from atexit import register
from urllib import response
from django.shortcuts import render

from applications.product.models import Product
from .serializers import ProcesoVentaSrializers
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from applications.order import serializers
from .models import Order, OrderDetail
# Create your views here.
