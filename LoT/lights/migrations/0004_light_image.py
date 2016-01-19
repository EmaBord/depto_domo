# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lights', '0003_light_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='light',
            name='image',
            field=models.ImageField(default=b'images/default.jpg', upload_to=b'images/'),
        ),
    ]
