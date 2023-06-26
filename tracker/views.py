from django.shortcuts import render
from .models import Task

def task_list_view(request):
    tasks = Task.objects.all()  # Получение всех задач из базы данных
    context = {'tasks': tasks}  # Передача данных в шаблон
    return render(request, 'tracker/task_list.html', context)