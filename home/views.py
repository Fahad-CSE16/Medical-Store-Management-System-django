import json
import random
from django.shortcuts import render
from django.template import RequestContext
from django.template import loader
from django.forms import formset_factory
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeForm, PasswordResetCompleteView, \
    PasswordResetConfirmView, PasswordResetView, PasswordResetForm, PasswordResetDoneView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
import time
from math import ceil
from django.views import generic, View
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from .models import Company, Product, Sales, Supplier,Contact
from .forms import *
from django.db.models import Q

def search(request):
    query = request.POST.get('q', '')
    if query:
        queryset = (Q(name__icontains=query)) | (Q(company__icontains=query)) | (Q(batch_no__icontains=query))
        products = Product.objects.filter(queryset).distinct()
    else:
       products = []
    
    return render(request, "home/product_list.html", {'products': products})

class HomeView(TemplateView):
    template_name = "home/home.html"


def logoutuser(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('home:homes')


def handleLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('home:homes')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="home/login.html",
                  context={"form": form})


def product_create(request):
    if request.method == "POST":
        form = FormForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            subcheck = Company.objects.filter(name=company)
            if not subcheck:
                Company.objects.create(name=company)
            subchecks = Product.objects.filter(name=name)
            if subchecks:
                messages.error(
                    request, 'Alreay this product has included to the list.!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            form.save()
            messages.success(request, 'Successfully added to the list.!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        company_list = Company.objects.all()
        form = FormForm(data_list=company_list)
    return render(request, 'home/product.html', {'form': form})


class ProductListView(generic.ListView):
    model = Product
    template_name = 'home/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('name')
class CompanyListView(generic.ListView):
    model = Company
    template_name = 'home/company_list.html'
    context_object_name = 'company'
    queryset = Company.objects.all().order_by('name')
class SupplierListView(generic.ListView):
    model = Supplier
    template_name = 'home/supplier_list.html'
    context_object_name = 'supplier'
    queryset = Supplier.objects.all().order_by('name')
class SalesListView(generic.ListView):
    model = Sales
    template_name = 'home/sales_list.html'
    context_object_name = 'sales'
    queryset = Sales.objects.all().order_by('name')

def delete(request,id):
    prod=Product.objects.filter(id=id)
    prod.delete()
    return redirect('home:product-list')

def addqty(request, pk):
    if request.method == "POST":
        qty=request.POST.get('qty')
        p = Product.objects.get(id=pk)
        p.qty = p.qty + int(qty)
        p.save()
    return redirect('home:product-list')
def makebill(request):
    if request.method == "POST":
        cart = request.POST.get('cart')
        price = request.POST.get('price')
        n = request.POST.get('name')
        phone = request.POST.get('phone')
        data = json.loads(cart)
        for c in data:
            name = c['name']
            qty = c['qty']
            prod = Product.objects.get(name=name)
            prod.qty = prod.qty - int(qty)
            if prod.qty <= 0:
                messages.warning(request, f'{prod.name} has finished')
                prod.delete()
            else:
                prod.save()
        p= Sales(items_json=cart, amount=price, name=n, phone=phone)
        p.save()
        total = price
    product = Product.objects.all().order_by('name')
    product_list = list(product.values('name', 'cost'))
    context = {}
    context["product"] = json.dumps(product_list)
    try:
        context["total"] = total
    except:
        pass
    return render(request, 'makebill.html', context)
from .forms import ProductForm
class EditProdView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'home/product.html'
    def get_success_url(self):
        id = self.kwargs['pk']
        return reverse_lazy('home:product-list')
class EditSupplierView(generic.UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'home/addsupplier.html'
    def get_success_url(self):
        id = self.kwargs['pk']
        return reverse_lazy('home:supplier-list')
class CreateSupplierView(generic.CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'home/addsupplier.html'
    def get_success_url(self):
        return reverse_lazy('home:supplier-list')
class CreateContactView(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'home/contact_us.html'
    def get_success_url(self):
        return reverse_lazy('home:product-list')