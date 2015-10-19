# -*- coding: utf-8 -*-
from django import forms
from .models import PruebaCampos, MuchasCategoria


class PruebaForm(forms.ModelForm):
    class Meta:
        model = PruebaCampos
        fields = ['rango_recha', 'fecha']


class MuchasCategoriaForm(forms.ModelForm):
    class Meta:
        model = MuchasCategoria
        fields = ["nombre"]
