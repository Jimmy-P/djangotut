# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_post_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='editor',
            field=models.ForeignKey(related_name='edits', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
