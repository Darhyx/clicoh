from re import T
from rest_framework import viewsets

from .models import Order, OrderDetail, Product

from rest_framework.response import Response
from .serializers import(
                         OrderSerializer,
                         OrderdetailSerializer,
                         ReportOrderDetailSerializers,
                         ProcesoVentaSrializers                        
                         )
from applications.order2 import serializers

class OrderViewSet(viewsets.ModelViewSet):
    
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderdetailViewSet(viewsets.ModelViewSet):
    
    serializer_class = OrderdetailSerializer
    queryset = OrderDetail.objects.all()

class RegisterOrderDetailViewset(viewsets.ViewSet):

    
   # serializer_class = ProcesoVentaSrializers
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        #recibo eñ post y des.serializo 
        serializer= ProcesoVentaSrializers(data=request.data)
        #valido los datos 
        serializer.is_valid(raise_exception=True)
        #
        #orderen = serializer.validated_data['data_time']
        orden = Order.objects.create(
            data_time=serializer.validated_data['data_time'],
        )
    
        #recupero productos
        products = serializer.validated_data['product']
        
        ordens_detail= []

        for product in products:
            prod = Product.objects.get(id=product['id'])
            #cuant =
            print('prod-----',prod)
            orden_detail= OrderDetail(
                order=orden,
                cuantity=product['cuantity'],
                product= prod,       
            )
            #
           
            ordens_detail.append(orden_detail)
        OrderDetail.objects.bulk_create(ordens_detail)
        return Response({'msj': 'Registro exitoso!'})


    def list(self, requiest):
        queryset = Order.objects.all()
        serializer= ReportOrderDetailSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        venta = Order.objects.get(id=pk)
       
        serializer =  ReportOrderDetailSerializers(venta)
        
        return Response(serializer.data)
    
    def delete(self, request, pk=None):
        venta = Order.objects.get(id=pk)
       
        serializer =  ReportOrderDetailSerializers(venta)
        
        return Response(serializer.data)
    
    
