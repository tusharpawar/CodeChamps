# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0012_solved'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Solved',
        ),
    ]
