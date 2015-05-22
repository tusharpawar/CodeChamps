# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0013_delete_solved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('challenge_name', models.CharField(unique=True, max_length=200)),
                ('challenge_body', models.TextField()),
                ('challenge_rules', models.TextField()),
                ('added_on', models.DateField(auto_now_add=True)),
                ('dp', models.ImageField(upload_to=b'competitions/')),
                ('problemlist', models.ManyToManyField(to='problems.problem')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Challenge',
                'verbose_name_plural': 'Challenges',
            },
            bases=(models.Model,),
        ),
    ]
