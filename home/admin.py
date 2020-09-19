from django.contrib import admin
from .models import Product, Company, Supplier, Stock, Sales
from django.contrib.admin import register
# Register your models here.

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Company)
admin.site.register(Stock)
admin.site.register(Sales)