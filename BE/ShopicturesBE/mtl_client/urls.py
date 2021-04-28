from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compute_stats', csrf_exempt(views.compute_stats), name='compute_stats'),
    path('compute_stats_file', csrf_exempt(views.compute_stats_file), name='compute_stats_file'),
    path('compute_stats_file_upload', csrf_exempt(views.compute_stats_file_upload), name='compute_stats_file_upload')
    ]