from ctypes import resize
from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from applications.product.models import Product
from . import managers

#from applications.product.models import Product
#
from .models import Order, OrderDetail

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            '__all__'

        )

class OrderdetailSerializer(serializers.ModelSerializer):
    '''Metodo para que actualice el stock'''
    '''Que no se repitan productos en el mismo pedido'''
    class Meta:
        model = OrderDetail
        fields = (
            '__all__'
        )

class ReportOrderDetailSerializers(serializers.ModelSerializer):
    products= serializers.SerializerMethodField()
    
    
   
    class Meta:
        model = Order
        fields = (
            'id',
            'data_time', 
            'products',
            #'total_ARS',
            #'total_USD',
        )
    def get_products(self, obj):
        #dame todos los productos de la tabl orderdetail con el id
        query_product = OrderDetail.objects.productos_por_venta(obj.id)

        product_serializars = OrderProductSerializer(query_product, many=True).data

        return product_serializars


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = (
            '__all__'
        )

class ProductDetailSerializers(serializers.Serializer):

    id= serializers.IntegerField()
    cuantity= serializers.IntegerField()

    def validate_cuantity(self, value):
        if value <= 0:
            raise serializers.ValidationError('cuantity debe ser mayor a 0')
        return value 
           
class ProcesoVentaSrializers(serializers.Serializer):

    data_time= serializers.DateTimeField()
    product= ProductDetailSerializers(many=True)
    
    

