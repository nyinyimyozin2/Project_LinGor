from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Customer)
admin.site.register(ShippingAddress)
admin.site.register(Order)
