from django.test import TestCase
from django.test import RequestFactory
from django.urls import reverse
from .. import views
from ..models import Image
import PIL

class ViewTestCase(TestCase):
    def setUp(self):
        img1 = PIL.Image.open(r"BE/shopictures/media/images_repository/Grass_and_mountains_again.jpg")
        img2 = PIL.Image.open(r"BE/shopictures/media/images_repository/lac.jpg")
        Image.objects.create(
                        name = "test_img_1",
                        owner = "tester",
                        price = 2000,
                        photo = InMemoryUploadedFile(img1, "test_img_1", "test_img_1" + ".jpg", 'image/jpeg', img1.tell, None)
                        )
        Image.objects.create(
                        name = "test_img_2",
                        owner = "tester",
                        price = 10000,
                        photo = InMemoryUploadedFile(img2, "test_img_2", "test_img_2" + ".jpg", 'image/jpeg', img2.tell, None)
                        )

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_add_image(self):
        pass

    def test_get_pictures(self): #TODO : Read this https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
        res = self.client.get('get_pictures?amount=2')
        self.assertTrue(resp.status_code == 200)

    def test_get_pictures_with_keyword(self):
        pass