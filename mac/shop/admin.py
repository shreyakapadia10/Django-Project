from django.contrib import admin

# Register your models here.

from . models import Product, Contact, Order, OrderTracker

# To register Product table
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderTracker)
