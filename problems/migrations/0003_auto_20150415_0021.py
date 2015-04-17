# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import problems.models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_remove_submissions_name1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='Code',
            field=models.FileField(null=True, upload_to=problems.models._upload_path, blank=True),
            preserve_default=True,
        ),
    ]
