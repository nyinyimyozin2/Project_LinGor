from django.shortcuts import render
from django.http import request
from django.core.handlers import exception

# Create your views here.
def index(request):
    return render(request,"index/index.html")

def about(request):
    return render(request,"index/about.html")

def page_404(request,exception):
    return render(request,'404.html', status=404)

def page_500(request):
    return render(request,'500.html', status=500)   
