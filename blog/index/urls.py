from django.contrib import admin
from django.urls import path,include,re_path
from .views import *


urlpatterns = [
    path('blog_main/',blog_main_views,name='blog_main'),
    path('login/',login_views,name='login'),
    path('',login_views),
    path('register/',register_views,name='register'),
    path('check_input/',check_input_views),
    path('check_input2/', check_input_views2),
    path('check_input3/', check_input_views3),
]


#增加网页跳转
urlpatterns +=[
    path('inheirt_page/',inheirt_page_views),
    path('about_me/',about_me_views),
]
