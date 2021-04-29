from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import ensure_csrf_cookie
import PIL
from io import BytesIO
from .models import Image
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
import json

@ensure_csrf_cookie
def add_image(request):
    if request.method == "POST":

        # img = request.body
        # stream = BytesIO(request.body)
        # buffer = BytesIO()
        # img = PIL.Image.open(stream)
        # img.save(fp=buffer, format='JPEG')
        img = ContentFile(BytesIO(request.body).getvalue())
        name = request.GET.get('name')
        img_file = Image.objects.create(
                        name = name,
                        owner = request.GET.get('owner'),
                        price = int(request.GET.get('price')),
                        photo = InMemoryUploadedFile(img, name, name + ".jpg", 'image/jpeg', img.tell, None)
                    )

        return HttpResponse("Image successfully uploaded!")