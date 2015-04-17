# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20150415_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='ip_tc',
            field=models.FileField(null=True, upload_to=b'input/', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='problem',
            name='op_tc',
            field=models.FileField(null=True, upload_to=b'output/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(unique=True, max_length=400),
            preserve_default=True,
        ),
    ]
