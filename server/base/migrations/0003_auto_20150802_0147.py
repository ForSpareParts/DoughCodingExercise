# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150802_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='exchange',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='symbol',
            field=models.CharField(max_length=10),
        ),
    ]
