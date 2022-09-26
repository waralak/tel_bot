from django.urls import path
import os
from . import views

urlpatterns = [
    path('{}/'.format(os.environ.get("TOKEN", "")), views.index),
]
