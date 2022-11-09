from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def login_view(request, *args, **kwargs):
    # TODO move to members project
    return render(request, 'login.html', {})
