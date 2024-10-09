from django.contrib import admin
from .models import Product, User
 
# Register your models here.
 
class ProductAdmin(admin.ModelAdmin):
   list_display = ('name', 'price', 'stock')

admin.site.register(Product)
#added 'user' page to /admin. delete created users here easily to purge sql database
admin.site.register(User)