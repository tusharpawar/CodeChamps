# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Developers', '0002_developer_ref_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='ref_id',
            field=models.CharField(default=b'ABC', max_length=100, null=True),
            preserve_default=True,
        ),
    ]
