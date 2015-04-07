# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Developers', '0003_auto_20150331_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='country',
            field=models.CharField(default=b'INDIA', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='developer',
            name='propic',
            field=models.ImageField(null=True, upload_to=b'profilepics/', blank=True),
            preserve_default=True,
        ),
    ]
