from django import forms
from .fields import ListTextWidget
from .models import Company, Product, Sales, Stock, Supplier
from django.forms import ModelForm, DateInput
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name',)
class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

class FormForm(ModelForm):
    company = forms.CharField(required=True)
    class Meta:
        model = Product
        fields= '__all__'
    def __init__(self, *args, **kwargs):
      _company_list = kwargs.pop('data_list', None)
      super(FormForm, self).__init__(*args, **kwargs)
      self.fields['company'].widget = ListTextWidget(data_list=_company_list, name='company-list')
