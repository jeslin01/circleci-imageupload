from django.test import TestCase
from django.test.client import RequestFactory
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from main_app import views
from django.test import override_settings

class MyViewTest(TestCase):
    def setUp(self):
        self.rq = RequestFactory()

    def test_view(self):
    	with open('test_data/images.jpg', 'rb') as img:
    		req = self.rq.post('my_view_url', {'my_post': 'data', 'test': 1, 'myfile': img})
    		resp = views.index(req)
    		print(resp)
    		self.assertEqual(resp.status_code, 200)

    def test_uploading_non_image_file_errors(self):
      # set up form data
      text_file = SimpleUploadedFile('front.txt', b'this is some text - not an image')

      req = self.rq.post('my_view_url', {'my_post': 'data', 'test': 1, 'myfile': text_file})
      resp = views.index(req)
      print(resp)
      self.assertEqual(resp.status_code, 400)