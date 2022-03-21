from django.db import models



class OrderDetailManager(models.Manager):

    def productos_por_venta(self, kword):
        query = self.filter(
            order__id= kword
        )
        return query
    
class OrderManager(models.Manager):

    pass