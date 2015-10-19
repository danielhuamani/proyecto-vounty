# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0002_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria',
            field=models.OneToOneField(related_name='one_categoria', null=True, to='pruebas.Categoria'),
        ),
    ]
