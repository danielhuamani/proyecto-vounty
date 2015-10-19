# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0003_auto_20151007_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='MuchasCategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120, verbose_name=b'nombre')),
                ('categoria', models.ForeignKey(related_name='mucha_categoria', blank=True, to='pruebas.MuchasCategoria', null=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.AlterField(
            model_name='categoria',
            name='categoria',
            field=models.OneToOneField(related_name='one_categoria', null=True, blank=True, to='pruebas.Categoria'),
        ),
    ]
