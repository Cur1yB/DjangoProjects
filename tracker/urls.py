from django.urls import path
from .views import task_list_view

urlpatterns = [
    path('tasks/', task_list_view, name='task-list'),
]
