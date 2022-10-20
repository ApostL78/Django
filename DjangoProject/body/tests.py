from django.test import TestCase

from body.models import Task


# add string here
# Create your tests here.
class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(title='title', task='task', views='100')
        Task.objects.create(title='title 2', task='task 2', views='0')

    def test_str_and_url(self):
        """Test __str__ and get_absolute_url methods"""
        home_url = '/'
        task1 = Task.objects.get(title='title')
        task2 = Task.objects.get(title='title 2')
        self.assertEqual(task1.__str__(), task1.title)
        self.assertEqual(task1.get_absolute_url(), home_url)

        self.assertEqual(task2.__str__(), task2.title)
        self.assertEqual(task2.get_absolute_url(), home_url)

# trying to modify last commit 2
# committing for rebase
# committing for rebase 2
