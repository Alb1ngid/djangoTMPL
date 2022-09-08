from django import forms
from .models import Order, Client



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address']

        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'contacts', 'description']



class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'contacts', 'description']


class OrderDeleteForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'contacts', 'description']

