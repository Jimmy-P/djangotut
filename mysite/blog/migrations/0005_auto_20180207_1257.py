# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180207_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(default=b'published', max_length=10, choices=[(b'published', b'Published'), (b'draft', b'Draft')]),
        ),
    ]
