from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('blog-details/<int:pk>', blog_details, name='blog-details'),
]
