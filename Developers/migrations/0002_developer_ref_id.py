# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Developers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='ref_id',
            field=models.CharField(default=b'ABC', max_length=100),
            preserve_default=True,
        ),
    ]
