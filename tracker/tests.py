
from django.test import TestCase
from django.urls import reverse
from tracker.models import Task

class TaskListViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('tasktracker:tasks')
        self.task1 = Task.objects.create(title='Task 1', description='Description 1')
        self.task2 = Task.objects.create(title='Task 2', description='Description 2')

    def test_task_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasktracker/tasks.html')
        self.assertContains(response, self.task1.title)
        self.assertContains(response, self.task2.title)

class TaskDeleteViewTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title='Task', description='Description')
        self.url = reverse('tasktracker:delete_tasks')

    def test_task_delete_view(self):
        response = self.client.post(self.url, data={'selected_tasks': [self.task.id]})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
        self.assertRedirects(response, reverse('tasktracker:tasks'))

class TaskModelTestCase(TestCase):
    def test_task_creation(self):
        title = 'Test Task'
        description = 'This is a test task'
        task = Task.objects.create(title=title, description=description)
        self.assertEqual(task.title, title)
        self.assertEqual(task.description, description)
