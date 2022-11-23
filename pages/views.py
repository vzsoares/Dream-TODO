from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    # sync localstorage items
    # create table item
    # send list via ajax
    return render(request, 'home.html', {})


def login_view(request, *args, **kwargs):
    return render(request, 'login.html', {})
