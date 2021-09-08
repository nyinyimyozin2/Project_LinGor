from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import *
from .models import *
import json
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user = request.user
        name = user.username
        email = user.email
        customer, created = Customer.objects.get_or_create(user=user, name=name, email=email)
        customer.save()
    items = Item.objects.all()
    data = {'items' : items}
    return render(request, "shop/shop.html", data)

def itemDetail(request, id):
    item = Item.objects.get(id=id)
    data = {'item': item}
    return render(request, "shop/itemDetail.html", data)

def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            User = form.save()
            return redirect('/shop/login')
        else:
            return redirect('/shop/signup')
    else:
        form = RegisterForm()
        
    return render(request, "shop/signup.html", {'form':form})   

def cart(request):
  
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    form = BillingForm()
    data = {'items' : items,'order':order, 'form':form}
    print(data)
    return render(request, "shop/cart.html",data)

def updateItem(request):
    data =json.loads(request.body)
    itemID = data['id']
    action = data['action']

    customer = request.user.customer
    item = Item.objects.get(id=itemID)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,item=item)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    if action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse(f"items been {action}",safe=False)

def checkout(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        address = form.data['address']
        state = form.data['state']
        city = form.data['city']
        zipcode = form.data['zipcode']
        customer = request.user.customer
        order = Order.objects.get(customer=customer,complete=False)
        item = order.orderitem_set.all()

        if form.is_valid() and item != None:
            shipping_address = ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = address,
                city = city,
                state = state,
                zipcode = zipcode
            )
            shipping_address.save()
            order.complete=True
            order.save()
            messages.success(request, "Transaction Completed")

    return redirect("/shop/cart")