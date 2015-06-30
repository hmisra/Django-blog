# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=500)),
                ('content', models.CharField(max_length=100000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
