# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Developers', '0007_auto_20150420_0923'),
        ('Challenges', '0002_auto_20150509_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='participents',
            field=models.ManyToManyField(to='Developers.Developer', null=True, blank=True),
            preserve_default=True,
        ),
    ]
