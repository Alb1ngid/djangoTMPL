from django.db import models
from client.models import Order


class Bottle(models.Model):
    description = models.TextField(blank=True)
    volume = models.IntegerField(default=10)
    maker = models.CharField(max_length=255)
    expired = models.BooleanField(default=True)

    orders = models.ManyToManyField(
        to=Order, blank=True,
        verbose_name='Orders',
        related_name='bottles'
    )

    def __str__(self):
        return f'{self.maker} - {self.volume}л'


class BottlesCount(models.Model):
    bottle = models.ForeignKey(to=Bottle, blank=True, on_delete=models.SET_NULL, related_name='bottle_count')
    count = models.IntegerField(default=0)
    order = models.ForeignKey(to=Order,blank=True, on_delete=models.SET_NULL, related_name='order')

    def __str__(self):
        return f'name: {self.bottle} - count: {self.count}'
