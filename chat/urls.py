# chat/urls.py
from django.conf.urls import url

from . import views

app_name = 'chat'

urlpatterns = [
    url('', views.index, name='index'),
]
