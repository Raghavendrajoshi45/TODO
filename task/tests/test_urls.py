from django.test import SimpleTestCase
from django.urls import reverse,resolve
from task.views import index,updateTask,deleteTask

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('list')
        
        self.assertEqual(resolve(url).func,index)


    def test_update_task_url_is_resolved(self):
        url = reverse('update_task')
        print(resolve(url))
        
      