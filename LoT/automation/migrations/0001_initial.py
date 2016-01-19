# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lights', '0005_remove_light_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encendido', models.CharField(max_length=100)),
                ('apagado', models.CharField(max_length=100)),
                ('luz', models.ForeignKey(related_query_name=b'automation', related_name='automations', to='lights.Light')),
            ],
        ),
    ]
