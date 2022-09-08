from django.shortcuts import render

from django.shortcuts import render, HttpResponse
from .models import Bottle


def makers_list(request):
    context = {}
    bottles_list = Bottle.objects.all()
    context["bottles_list"] = bottles_list
    html_page = render(request, 'makers.html', context)
    return html_page