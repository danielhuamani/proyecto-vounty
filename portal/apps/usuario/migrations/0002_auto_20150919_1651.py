# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['usuario']},
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombres',
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(default='', max_length=120, verbose_name=b'usuario'),
            preserve_default=False,
        ),
    ]
