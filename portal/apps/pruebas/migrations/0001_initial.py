# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.ranges


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PruebaCampos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rango_recha', django.contrib.postgres.fields.ranges.DateRangeField()),
                ('fecha', models.DateField()),
            ],
            options={
                'verbose_name': 'PruebaCampos',
                'verbose_name_plural': 'PruebaCamposs',
            },
        ),
    ]
