from dataclasses import field
from pyexpat import model
from rest_framework import serializers

#from applications.product.models import Product
#
from .models import Product

class PorductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = (
            '__all__'
         )