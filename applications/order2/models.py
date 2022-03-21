from django.db import models

# Create your models here.

#
from applications.product.models import Product
#managers
from .managers import OrderDetailManager, OrderManager
from django.db.models.signals import post_delete

class Order(models.Model):
    data_time = models.DateTimeField()
    

    def __str__ (self):
        return 'Orden: '+ str(self.id) + ' Fecha ' + str(self.data_time)
    def get_total(self, cuant, price):

        total= cuant * price
        return total
    objects = OrderManager()
class OrderDetail(models.Model):
    order = models.ForeignKey(
            Order, 
            on_delete= models.CASCADE,
            related_name= 'order_orderdetail'
            )
    cuantity = models.PositiveIntegerField(
            
            )
    product = models.ForeignKey(
            Product,
            on_delete= models.CASCADE
            )
    objects = OrderDetailManager()

    def save(self, *args, **Kwargs):
        self.product.stock = self.product.stock -self.cuantity
        self.product.save()
        
        super(OrderDetail, self).save(*args, **Kwargs)

    def  __str__ (self):
        return str(self.order) + ' Cantidad: ' + str(self.cuantity) + ' Producto: ' + str(self.product)

def update_product_stock(sender, instance, **kwargs):
    instance.product.stock = instance.product.stock + instance.cuantity
    instance.product.save()
post_delete.connect(update_product_stock, sender=OrderDetail)

