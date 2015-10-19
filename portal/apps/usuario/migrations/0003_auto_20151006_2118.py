# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20150919_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(unique=True, max_length=120, verbose_name=b'usuario'),
        ),
    ]
