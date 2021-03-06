# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 06:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('meta_description', models.CharField(blank=True, max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('published', 'published'), ('draft', 'draft'), ('staged', 'staged')], max_length=20)),
                ('content', models.TextField(blank=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='page.Page')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
