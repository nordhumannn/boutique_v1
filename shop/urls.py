from django.urls import path
from .views import product_list, products_in_category, product_detail
from base.views import base

app_name = 'shop'

urlpatterns = [
    path('all/', product_list, name='product_list'),
    path('', base),
    path('all/<str:slug>/', products_in_category, name='products_in_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
]