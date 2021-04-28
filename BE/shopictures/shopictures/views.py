from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Image
import json

@ensure_csrf_cookie
def add_image(request):
    if request.method == "POST":
        print(f"file : {request.body}")
        img = json.loads(request.body)

        img_file = Image.objects.create(
                        name = img['name'],
                        owner = img['owner'],
                        price = img['price'],
                        photo = img['photo']
                    )

        # img_file.photo = "images_repository" + str(img_file.id) + img['name'] + ".jpg"

        #TODO test png

        # img_file.save()

        return HttpResponse("Image successfully uploaded!")