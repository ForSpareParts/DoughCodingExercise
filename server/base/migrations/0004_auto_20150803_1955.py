# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20150802_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockprice',
            name='company',
        ),
        migrations.DeleteModel(
            name='StockPrice',
        ),
    ]
