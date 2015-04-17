# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qCode', models.CharField(unique=True, max_length=200)),
                ('title', models.CharField(max_length=400)),
                ('body', models.TextField()),
                ('added_on', models.DateField(auto_now_add=True)),
                ('input_format', models.TextField()),
                ('output_format', models.TextField()),
            ],
            options={
                'ordering': ['-qCode'],
                'verbose_name': 'Problem',
                'verbose_name_plural': 'Problems',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name1', models.CharField(max_length=200)),
                ('Code', models.FileField(null=True, upload_to=b'submissions/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
