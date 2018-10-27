from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('blog_main/',blog_main_views,name='blog_main'),
    path('login/',login_views,name='login'),
    path('',login_views),
    path('register/',register_views,name='register'),
]
