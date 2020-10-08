from django.contrib import admin
from django.urls import path, include

from .views import *
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='homes'),
    path('logout/', logoutuser, name='logout'),
    path('login/', handleLogin, name='login'),
    path('create/', product_create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('add/<int:pk>/', addqty, name='add'),
    path('edit/<int:pk>/',EditProdView.as_view(), name='edit'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('makebill/', makebill, name='makebill'),
    # path('create/', ProductCreate.as_view(), name='create'),


]
