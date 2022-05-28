from django.db import models
from accounts.models import Account
from store.models import Product


# Create your models here.
class Order(models.Model):

    order_number   = models.CharField(max_length=1000)
    user           = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    your_name      = models.CharField(max_length=20)
    last_name      = models.CharField(max_length=20)
    email          = models.EmailField(max_length = 254)
    phone          = models.CharField(max_length=20)
    address1       = models.CharField(max_length=20)
    address2       = models.CharField(max_length=20)
    city           = models.CharField(max_length=20)
    state          = models.CharField(max_length=20)
    country        = models.CharField(max_length=20)
    order_note     = models.CharField(max_length=20)

    def full_name(self):
        return f'{self.your_name} {self.last_name}'

    def full_add(self):
        return f'{self.address1} {self.address2}'





    def __str__(self):
        return self.your_name

# class OrderProduct():
#     pass
