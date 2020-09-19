from django.contrib import admin
from django.urls import path, include

from .views import *
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='homes'),
    path('logout/', logoutuser, name='logout'),
    path('login/', handleLogin, name='login'),
    path('create/', product_create, name='create'),
    # path('create/', ProductCreate.as_view(), name='create'),
   

]
