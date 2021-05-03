from django.test import TestCase
from django.test import RequestFactory
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile

from .. import views
from ..models import Image
import PIL
import json

def is_same_img(response_img, test_image):
    return response_img['fields']['name'] == test_image.name and \
           response_img['fields']['owner'] == test_image.owner and \
           int(float(response_img['fields']['price'])) == int(float(test_image.price))

class ViewTestCase(TestCase):
    def setUp(self):
        self.img1 = Image.objects.create(
                        name = "test_img_1",
                        owner = "tester",
                        price = 2000,
                        photo = r"BE/shopictures/media/images_repository/Grass_and_mountains_again.jpg"
                    )
        self.img2 = Image.objects.create(
                        name = "test_img_2",
                        owner = "tester",
                        price = 10000,
                        photo = r"BE/shopictures/media/images_repository/lac.jpg"
                    )

    def tearDown(self):
        Image.objects.all().delete()

    def test_add_image(self):
        test_img3= {'fields' : {'name': 'test_img_3', 'owner': 'tortue_tester', 'price': '8000', 'photo' : r"BE/shopictures/media/images_repository/ski.jpg"}}

        res = self.client.post('/add_image', data={'name': 'test_img_3', 'owner': 'tortue_tester', 'price': '8000', 'photo' : r"BE/shopictures/media/images_repository/ski.jpg"})

        self.assertTrue(res.status_code == 200)
        img = Image.objects.filter(name__contains='test_img_3')
        self.assertTrue(is_same_img(test_img3, img[0]))


    def test_get_pictures_with_2_pictures(self):
        res = self.client.get('/get_pictures?amount=2')
        pictures = json.loads(res.content)

        self.assertTrue(res.status_code == 200)
        self.assertTrue(len(pictures) == 2)
        self.assertTrue(is_same_img(pictures[1], self.img1))
        self.assertTrue(is_same_img(pictures[0], self.img2))
        

    def test_get_pictures_with_1_picture(self):
        res = self.client.get('/get_pictures?amount=1')
        pictures = json.loads(res.content)

        self.assertTrue(res.status_code == 200)
        self.assertTrue(len(pictures) == 1)
        self.assertTrue(is_same_img(pictures[0], self.img2))
        

    def test_get_pictures_with_0_picture(self):
        res = self.client.get('/get_pictures?amount=0')
        pictures = json.loads(res.content)

        self.assertTrue(res.status_code == 200)
        self.assertTrue(len(pictures) == 0)
        

    def test_get_pictures_with_keyword_should_return_2_pictures(self):
        res = self.client.get('/get_pictures_with_keyword?keyword=test')
        pictures = json.loads(res.content)

        self.assertTrue(res.status_code == 200)
        self.assertTrue(len(pictures) == 2)
        self.assertTrue(is_same_img(pictures[0], self.img1))
        self.assertTrue(is_same_img(pictures[1], self.img2))
        

    def test_get_pictures_with_keyword_should_return_1_picture(self):
        res = self.client.get('/get_pictures_with_keyword?keyword=img_1')
        pictures = json.loads(res.content)

        self.assertTrue(res.status_code == 200)
        self.assertTrue(len(pictures) == 1)
        self.assertTrue(is_same_img(pictures[0], self.img1))
        

    def test_get_pictures_with_not_present_keyword_should_return_0_pictures(self):
        res = self.client.get('/get_pictures_with_keyword?keyword=sdgsf')
        pictures = json.loads(res.content)

        self.assertTrue(res.status_code == 200)
        self.assertTrue(len(pictures) == 0)