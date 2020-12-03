from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name
    def query_set(self):
        return Category.objects.all()

class Product(models.Model):
    productName = models.CharField(max_length=50)
    productPrice = models.IntegerField()
    productDesc = models.CharField(max_length = 600)
    productImg = models.URLField(max_length = 300)
    productCategory = models.ForeignKey(Category , on_delete=models.CASCADE)
    def __str__(self):
        return self.productName

class Order(models.Model):
    orderCustomer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    orderProduct = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    orderDate = models.DateField(auto_now_add=True)
    isComplete = models.BooleanField(default=False, null=True, blank=False)
    
    def __str__(self):
        return str(self.pk)
    
    @property
    def get_total_price(self):
        totalitems = self.orderitem_set.all()
        total_price = sum([item.get_total for item in totalitems])
        return total_price

    @property
    def get_total_item(self):
        totalitems = self.orderitem_set.all()
        total_item = sum([item.oiQuantity for item in totalitems])
        return total_item
    


class OrderItem(models.Model):
    oiProduct = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    oiOrder = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    oiQuantity = models.IntegerField(default=0, null=True, blank=True)
    oiDate = models.DateField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.oiProduct.productPrice * self.oiQuantity
        return total

class CustomerAddress(models.Model):
    caCustomer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    caOrder = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    caProvince = models.CharField(max_length=20, null = True)
    caCity = models.CharField(max_length=50, null = True)
    caAddress = models.CharField(max_length=100, null = True)
    caDate = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Customer Addresses"
    def __str__(self):
        return self.caAddress



    