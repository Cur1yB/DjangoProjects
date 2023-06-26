# tasktracker/views.py
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

def delete_tasks(request):
    if request.method == 'POST':
        selected_tasks = request.POST.getlist('selected_tasks')
        Task.objects.filter(id__in=selected_tasks).delete()
    return redirect('tasktracker:tasks')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tracker/create_task.html', {'form': form})


def task_list_view(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    
    else:
        form = TaskForm()


    context = {'tasks': tasks, 
               'form': form,
               }  
    return render(request, 'tracker/task_list.html', context)

def tasks_view(request):
    #tasks = Task.objects.filter(deadline__gt=datetime.date.today()) # дэдлайн больше текущей даты
    tasks = Task.objects.all()
    return render(request, 'tracker/tasks.html', {'tasks': tasks})