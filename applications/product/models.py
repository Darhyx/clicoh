from pyexpat import model
from sqlite3 import Timestamp

from django.db import models

# Create your models here.
class Product(models.Model):
  
    name = models.CharField(
        'Nombre',
        max_length=50
        )
    price = models.FloatField(
        'Precio',
        max_length=3,
        

        )
    stock = models.IntegerField(
        'Stock',
        
        )
    
    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - '