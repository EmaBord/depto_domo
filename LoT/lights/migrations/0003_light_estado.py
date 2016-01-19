# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lights', '0002_remove_light_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='light',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
