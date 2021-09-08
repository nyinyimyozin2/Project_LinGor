from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email","password1", "password2"]

class BillingForm(forms.Form):
    METHODS = [
        ('1','Paypal'),
        ('2','Visa')
    ]
    address = forms.CharField(max_length=200)
    state = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    zipcode = forms.IntegerField(max_value=99999)
    payment_method = forms.ChoiceField(choices=METHODS,required=True)
    class Meta:
        model = ShippingAddress
        fields = ["address", "city", "zipcode", "payment_method"]
    