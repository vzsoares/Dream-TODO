from django.shortcuts import render
from django.http import JsonResponse

from .models import UserTodo

# Create your views here.


def getUserTodos(request):
    if request.user.is_authenticated:
        todos = UserTodo.objects.all().filter(owner__username='bob')
        return JsonResponse({'todos': list(todos.values('todos'))})
    else:
        return JsonResponse({})
