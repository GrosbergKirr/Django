from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('create', create),
    path('geturl', geturl),
    # path('response', response)
]