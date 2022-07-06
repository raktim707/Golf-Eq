from django.urls import path
from . import views
from shop.dash_apps.finished_apps import *


app_name = 'shop'
urlpatterns = [
    path('', views.home, name="home"),
    path('dash-app/<int:id>/', views.dashApps, name='dash_app'),
    path('product-list/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,  name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]