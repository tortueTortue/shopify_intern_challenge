from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import PIL
from io import BytesIO
from .models import Image
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core import serializers
import json

@ensure_csrf_cookie
def add_image(request):
    if request.method == "POST":

        img = ContentFile(BytesIO(request.body).getvalue())
        req = request.GET
        name = req.get('name')
        if not name:
            name = request.POST.get('name')
            req = request.POST

        img_file = Image.objects.create(
                        name = name,
                        owner = req.get('owner'),
                        price = int(req.get('price')),
                        photo = InMemoryUploadedFile(img, name, name + ".jpg", 'image/jpeg', img.tell, None)
                    )

        return HttpResponse("Image successfully uploaded!")

# @ensure_csrf_cookie
def get_pictures(request):
    if request.method == "GET":
        img_locations = Image.objects.all().order_by('-id')[:int(request.GET.get('amount'))]
        img_locations_json = serializers.serialize('json', img_locations)

        return HttpResponse(img_locations_json, content_type ="application/json")

def get_pictures_with_keyword(request):
    if request.method == "GET":
        # choose random pics
        img_locations = Image.objects.all().filter(name__contains=str(request.GET.get('keyword')))
        img_locations_json = serializers.serialize('json', img_locations)

        return HttpResponse(img_locations_json, content_type ="application/json")