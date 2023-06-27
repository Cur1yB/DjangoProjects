from django.urls import path
from .views import task_list_view, tasks_view, delete_tasks
app_name = 'tasktracker'
urlpatterns = [
    path('new_task/', task_list_view, name='task-list'),
    path('all_tasks/', tasks_view, name='tasks'),
    path('delete_tasks/', delete_tasks, name='delete_tasks')
]
