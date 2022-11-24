from django.shortcuts import render
from django.http import JsonResponse

from .models import UserTodo

# Create your views here.


def getUserTodos(request):
    if request.user.is_authenticated:
        todos = UserTodo.objects.all().filter(owner__username='bob')
        return JsonResponse({'todos': list(todos.values('todos'))}, status=200)
    else:
        return JsonResponse({}, status=400)


def updateTodos(request):
    if request.method == "POST":
        # TODO save to db
        # TODO check if user is auth
        print(request.POST['data'])
        return JsonResponse({})
    else:
        return JsonResponse({})
