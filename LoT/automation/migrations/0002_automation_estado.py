# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='automation',
            name='estado',
            field=models.CharField(default=datetime.datetime(2016, 1, 20, 16, 24, 35, 837567, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
