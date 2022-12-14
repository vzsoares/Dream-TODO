from django.shortcuts import render
from django.http import JsonResponse

from .models import UserTodo

# Create your views here.


def getUserTodos(request):
    if request.user.is_authenticated:
        todos = UserTodo.objects.all().filter(owner__username=request.user)
        return JsonResponse({'todos': list(todos.values('todos'))}, status=200)
    else:
        return JsonResponse({}, status=400)


def updateTodos(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            data = request.POST['data']
            try:
                prevTodo = UserTodo.objects.get(owner__username=request.user)
                prevTodo.todos = data
                prevTodo.save()
            except:
                newTodo = UserTodo(owner=request.user, todos=data)
                newTodo.save()
            return JsonResponse({})
        else:
            return JsonResponse({}, status=400)
    else:
        return JsonResponse({}, status=400)
