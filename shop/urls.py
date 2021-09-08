from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name="shop"),
    path('update_item',views.updateItem,name="shop-updateItem"),
    path('cart',views.cart,name="shop-cart"),
    path('item/<int:id>', views.itemDetail, name="shop-itemDetail"),
    path('checkout',views.checkout,name="shop-checkout"),
    path('register',views.register,name="shop-register"),
    path('login',auth_views.LoginView.as_view(template_name="shop/signin.html"),name="shop-login"),
    path('logout',auth_views.LogoutView.as_view(template_name="shop/logout.html"),name="shop-logout"),
]