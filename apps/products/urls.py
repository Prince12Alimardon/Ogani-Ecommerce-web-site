from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', home, name='home'),
    path('shop-details/<int:pid>', shop_details, name='shop-details'),
    path('shop-grid/', shop_grid, name='shop_grid'),
]
