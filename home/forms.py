from django import forms
from .fields import ListTextWidget
from .models import Company, Product, Sales, Supplier,Contact
from django.forms import ModelForm, DateInput


class FormsetForm(forms.Form):
    delete = forms.BooleanField(required=False, initial=False)
    # some other fields with data
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name',)
class QtyForm(forms.Form):
    value = forms.IntegerField()
class BillForm(ModelForm):
    name= forms.CharField(required=True)
    class Meta:
        model = Product
        fields=('name',)

    def __init__(self, *args, **kwargs):
      _company_list = kwargs.pop('data_list', None)
      super(BillForm, self).__init__(*args, **kwargs)
      self.fields['name'].widget = ListTextWidget(
          data_list=_company_list, name='name-list')
class FormForm(ModelForm):
    company = forms.CharField(required=True)
    mfg = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', }))
    exp = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', }))
    class Meta:
        model = Product
        fields= '__all__'
    def __init__(self, *args, **kwargs):
      _company_list = kwargs.pop('data_list', None)
      super(FormForm, self).__init__(*args, **kwargs)
      self.fields['company'].widget = ListTextWidget(data_list=_company_list, name='company-list')
class ProductForm(ModelForm):
    mfg = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', }))
    exp = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', }))
    class Meta:
        model = Product
        fields= ('mfg','exp','cost','selling_price','qty','supplier')
class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields= '__all__'
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields= '__all__'
   
