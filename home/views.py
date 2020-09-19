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
from django.views.generic import View,TemplateView
import time
from math import ceil
from django.views import generic, View
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from .models import Company, Product, Stock, Sales, Supplier
from .forms import ProductForm,StockForm,FormForm

# from tolet.models import Post, PostFile
# from person.models import Subject, District, Classes
# from person.forms import ContactForm
# from person.models import UserProfile, Contact
# from posts.templatetags import extras

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
        if  form.is_valid():
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            subcheck = Company.objects.filter(name=company)
            if  not subcheck:
                Company.objects.create(name=company)
            subchecks = Product.objects.filter(name=name, company=company)
            if  subchecks:
                messages.error(request, 'Alreay this product has included to the list.!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            Product.objects.create(name=name, company=company)
            messages.success(request, 'Successfully added to the list.!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        company_list = Company.objects.all()
        form = FormForm(data_list=company_list)
    return render(request, 'home/product.html', {'form':form})






# class ProductCreate(generic.CreateView):
#     model = Product
#     form_class = ProductForm
#     # success_url = 'home:homes'
#     template_name = 'home/product.html'

#     def form_valid(self, form):
#         name = form.cleaned_data['name']
#         # product=form.cleaned_data['product']
#         company = form.cleaned_data['company']
#         subcheck = Company.objects.filter(name=company)
#         if not subcheck:
#             Company.objects.create(name=company)
#         subchecks = Product.objects.filter(name=name)
#         if subcheck:
#             messages.error(
#                 self.request, 'Alreay this product has included to the list.!')
#             return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
#         messages.success(self.request, 'Successfully Created A product')
#         return super(ProductCreate, self).form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy('home:homes')
