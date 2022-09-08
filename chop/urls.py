"""chop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from client.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('info/', info),
    path('makers/', MakersListView.as_view()),
    path('clients/', ClientListView.as_view(), name='clients-list'),
    path('client/<int:id>/', ClientDetailView.as_view(), name="client-detail"),
    path('client/update/<int:id>/', ClientUpdateView.as_view(), name="client-update"),
    path('order/create/', CreateOrderDjangoView.as_view(), name="order-djangoform"),
    path('orders/', OrdersListView.as_view(), name='orders-list'),
    path('order/<int:id>/', OrderDetailView.as_view(), name="order-detail"),
    path('order/update/<int:id>/', OrderUpdateView.as_view(), name="order-update"),
    path('order/delete/<int:id>/', OrderDeleteView.as_view(), name="order-delete"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)