# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Developers', '0006_delete_solved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='problems_list',
            field=models.CharField(max_length=2000, null=True),
            preserve_default=True,
        ),
    ]
