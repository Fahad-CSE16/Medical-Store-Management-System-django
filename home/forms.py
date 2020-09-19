from django import forms
from .fields import ListTextWidget
from .models import Company, Product, Sales, Supplier
from django.forms import ModelForm, DateInput
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name',)
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
