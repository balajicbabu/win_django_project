# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20151008_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=8, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 8, 16, 53, 11, 40000, tzinfo=utc)),
        ),
    ]
