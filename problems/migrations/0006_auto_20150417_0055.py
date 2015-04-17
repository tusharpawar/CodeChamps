# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_solved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['-id'], 'verbose_name': 'Problem', 'verbose_name_plural': 'Problems'},
        ),
        migrations.RemoveField(
            model_name='problem',
            name='qCode',
        ),
    ]
