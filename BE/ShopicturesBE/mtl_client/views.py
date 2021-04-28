from __future__ import absolute_import, unicode_literals

from celery import shared_task

import threading
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from .tasks import start_client, get_msg, run_mtl_client, compute_stats_task, compute_stats_file_task, check_health, compute_stats_file_upload_task
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
import json


def index(request):
   start_client.delay()
   return HttpResponse(200)

@ensure_csrf_cookie
def compute_stats(request):
   body = json.loads(request.body.decode('utf-8'))
   print(f"string :{body}")
   if request.method == "POST":
      if check_health() :
         print(f"ag : {body['agregators']}")
         compute_stats_task.delay(body['topics'], body['agregators'])
         return HttpResponse("Calcul de statisque correctement commencé")
      
      return HttpResponseServerError

@ensure_csrf_cookie
def compute_stats_file(request):
   print(f"path : {request.body}")
   str_body = "{" + str(request.body).split('{')[1][:-1]
   body = json.loads(str_body)
   if request.method == "POST":
      compute_stats_file_task(body['fileName'])
      return HttpResponse(200)

@ensure_csrf_cookie
def compute_stats_file_upload(request):
   print(f"file : {request.body}")
   
   if request.method == "POST":
      return HttpResponse(compute_stats_file_upload_task(request.body))
