from django.db import models
from django.contrib.auth.models import User
class Client(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.SET_NULL, blank=True, related_name='client')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, verbose_name='adres', blank=True)
    active = models.BooleanField(default=True)
    bottles_ordered = models.IntegerField(default=1, verbose_name="Количество бутылок")
    photo = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    client = models.ForeignKey(to=Client, blank=True, on_delete=models.SET_NULL, related_name='order')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="создания заказа")
    updated_at = models.DateTimeField( auto_now=True,verbose_name="изменения заказа")
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name