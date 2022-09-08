from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .models import Client, Order
from core.models import Bottle
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import OrderForm, OrderUpdateForm, OrderDeleteForm, ClientForm


def contacts(request):
    return render(request, "contacts.html")


def info(request):
    return render(request, "info.html")


class ClientListView(ListView):
    model = Client
    template_name = 'client/clients.html'


# def clients_list(request):
#     context = {}
#     bottles_list = Client.objects.all()
#     context["clients_list"] = bottles_list
#     html_page = render(request, 'clients.html', context)
#     return html_page


class MakersListView(ListView):
    model = Bottle
    template_name = 'makers.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = "client/client_info.html"


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client/client_update.html'
    fields = ['name', 'address']
    success_url = '/clients/'



class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_info.html'


class CreateOrderView(View):
    def post(self, request):
        data = request.POST
        order = Order()
        order.name = data["name"]
        order.contacts = data["contacts"]
        order.description = data["description"]
        order.save()
        return HttpResponse("Форма обработана")

    def get(self, request):
        return render(request, 'order/order_form.html')


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order/order_update.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/order/'

class CreateOrderDjangoView(CreateView):
    model = Order
    template_name = 'order/order_djangoform.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/order/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['our_number'] = 1
        return context


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/order_delete.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/order/'



class OrdersListView(ListView):
    model = Order
    template_name = 'order/order.html'
