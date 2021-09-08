from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name =models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    ITEM_TYPE = [
        ('PH','Phone'),
        ('TB','Tablet'),
        ('LT','Laptop'),
    ]
    name =models.CharField(max_length=200,null=True)
    price = models.FloatField()
    description = models.TextField(null=True)
    thumbnail = models.ImageField(null=True, blank=True)
    type = models.CharField(max_length=2, choices=ITEM_TYPE,default='PH')

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now)
    complete = models.BooleanField(default=False,null=True,blank=False)

    def __str__(self):
        return str(self.id)
    @property
    def total_order_price(self):
        orderitems = self.orderitem_set.all()
        total = sum(item.total_item_price for item in orderitems)
        return total

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(default=datetime.now)

    @property
    def total_item_price(self):
        total = self.item.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.address










