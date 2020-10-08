from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    phone=models.CharField(max_length=17,default='')
    email=models.EmailField(default='')
    def __str__(self):
        return self.name 
class Product(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    batch_no = models.CharField(max_length=25)
    cost = models.IntegerField()
    selling_price = models.IntegerField()
    qty=models.IntegerField()
    mfg = models.DateField()
    exp = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="supplier_set")
    class Meta:
        ordering= ('name',)
    def __str__(self):
        return self.name
from django.utils.timezone import now
class Sales(models.Model):
    items_json = models.CharField(max_length=900)
    amount = models.IntegerField(default=0)
    name=models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    time=models.DateTimeField(default=now)
    def __str__(self):
        return self.name+ "-" + str(self.amount) + "TK"
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=17)
    email=models.EmailField()
    details=models.TextField()
    def __str__(self):
        return self.name
    
