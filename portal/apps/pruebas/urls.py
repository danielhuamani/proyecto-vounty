# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^prueba/$', views.prueba, name='prueba'),
    url(r'^categorias/$', views.categorias, name='categorias'),
]
