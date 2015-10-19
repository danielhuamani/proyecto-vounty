# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.postgres.fields import DateRangeField, HStoreField


class PruebaCampos(models.Model):
    rango_recha = DateRangeField()
    fecha = models.DateField()

    class Meta:
        verbose_name = "PruebaCampos"
        verbose_name_plural = "PruebaCamposs"

    def __unicode__(self):
        return str(self.rango_recha)


class Categoria(models.Model):
    nombre = models.CharField("nombre", max_length=120)
    categoria = models.OneToOneField("self", related_name='one_categoria', null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.nombre


class MuchasCategoria(models.Model):
    nombre = models.CharField("nombre", max_length=120)
    categoria = models.ForeignKey("self", related_name='mucha_categoria', null=True, blank=True)

    class Meta:
        verbose_name = "MuchasCategoria"
        verbose_name_plural = "MuchasCategorias"

    def __unicode__(self):
        return self.nombre
