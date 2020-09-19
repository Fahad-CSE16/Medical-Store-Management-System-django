from django.contrib import admin
from django.urls import path, include
from . import views

from .views import *
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='homes'),
    path('logout/', logoutuser, name='logout'),
    path('login/', handleLogin, name='login'),
    path('ccreate/', product_create, name='ccreate'),

]
