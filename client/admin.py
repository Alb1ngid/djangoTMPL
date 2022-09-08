from django.contrib import admin


from .models import Order,Client




class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['name', 'address', 'bottles_ordered', 'user']
    list_editable = ['bottles_ordered']
    fields = ['user', 'name', 'address', 'active', 'bottles_ordered', 'photo']


admin.site.register(Client, ClientAdmin)


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['contacts', 'created_at', 'updated_at']
    model = Order
    list_display = ['name', 'contacts', 'created_at', 'finished']
    list_editable = ['contacts', 'finished']
    fields = ['name', 'contacts', 'created_at', 'updated_at', 'description', 'finished']


admin.site.register(Order, OrderAdmin)
