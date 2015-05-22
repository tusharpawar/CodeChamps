# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Challenges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name=b'Event End Time', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='challenge',
            name='start_time',
            field=models.DateTimeField(null=True, verbose_name=b'Event start Time', blank=True),
            preserve_default=True,
        ),
    ]
