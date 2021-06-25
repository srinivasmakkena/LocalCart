from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
#from django.contrib.auth import views as vw
admin.site.site_header = 'LocalCart Administration'                    # default: "Django Administration"
admin.site.index_title = 'Admin Controls'                 # default: "Site administration"
admin.site.site_title = 'LocalCart'
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('addproduct', views.addproduct, name="addproduct"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('category/<str:pk_test>/', views.category, name="category"),
    path('dash', views.dashboard, name='dashboard'),
    path('logout/',views.logt,name="logout"),
    path('location', views.location, name='location'),
    path('error', views.error, name='error'),
    path('checkout', views.checkout, name='checkout'),
    path('login', views.flogin, name='login'),
    path('cart/<str:pk>', views.cart, name='cart'),
    path('cartdel/<str:pk>', views.cartdel, name='cartdel'),
    path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('admin/', admin.site.urls),
    path('seller', views.seller,name="seller"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('delete_product/<str:pk>/', views.deleteproduct, name="delete_product"),
    path('shops/<str:pk_test>/', views.shops, name="shops"),
    path('orders/<str:pk>/',views.orders,name='orders')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)