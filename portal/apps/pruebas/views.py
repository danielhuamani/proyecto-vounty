# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext as ctx
from django.core.urlresolvers import reverse, reverse_lazy
from .models import PruebaCampos, Categoria, MuchasCategoria
from .forms import PruebaForm, MuchasCategoriaForm
from psycopg2.extras import DateRange
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

def prueba(request):
    # prueba = PruebaCampos.objects.filter(rango_recha__contains=NumericRange(10-10-10, 10-10-10))
    # print prueba[0].rango_recha
    categorias_abuelo = MuchasCategoria.objects.all()
    return render_to_response('pruebas.html', locals(), context_instance=ctx(request))


def categorias(request):
    categorias_abuelo = MuchasCategoria.objects.all()
    # print categorias_abuelo
    if request.method == "POST":
        form = MuchasCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("pruebas:categorias"))
    else:
        form = MuchasCategoriaForm()
    # categoria_padre = categorias_abuelo[0].mucha_categoria.all()
    return render_to_response('portal/categorias.html', locals(), context_instance=ctx(request))
