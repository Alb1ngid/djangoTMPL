from django.contrib import admin

from .models import Bottle, BottlesCount

admin.site.register(Bottle, BottleAdmin)

class BottleAdmin(admin.ModelAdmin):
    model = Bottle
    list_display = ['maker', 'volume', 'expired']
    list_editable = ['expired']
    fields = ['maker', 'volume', 'description', 'expired']




class BottleCountAdmin(admin.ModelAdmin):
    model = BottlesCount
    list_editable = ['count']
    list_display = ['order', 'bottle', 'count']
    fields = ['bottle', 'count', 'order']


admin.site.register(BottlesCount, BottleCountAdmin)