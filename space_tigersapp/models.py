from django.db import models

# Create your models here.
class Product(models.Model):
   name = models.CharField(max_length=255)
   price = models.FloatField()
   stock = models.IntegerField()
   image_url = models.CharField(max_length=2083)

class User(models.Model):
   first_name = models.CharField(max_length=30)
   middle_initial = models.CharField(max_length=1, blank=True, null=True)
   last_name = models.CharField(max_length=30)
   email = models.EmailField()
   phone = models.CharField(max_length=15)
   avatar_url = models.URLField(max_length=2083)