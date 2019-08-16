# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-08-11 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190811_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.Comments'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='body',
            field=models.TextField(max_length=256, verbose_name='Comment here'),
        ),
    ]
