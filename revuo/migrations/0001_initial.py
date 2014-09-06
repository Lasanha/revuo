# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import revuo.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('editor', models.BooleanField(default=False)),
                ('about', models.TextField(max_length=1024)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('authorized', models.BooleanField(default=False)),
                ('title', models.TextField(max_length=140)),
                ('description', models.TextField(max_length=280)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(to='revuo.Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('authorized', models.BooleanField(default=False)),
                ('title', models.TextField(max_length=140)),
                ('description', models.TextField(max_length=280)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(to='revuo.Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('authorized', models.BooleanField(default=False)),
                ('title', models.TextField(max_length=140)),
                ('description', models.TextField(max_length=280)),
                ('attachment', models.FileField(upload_to=revuo.models.publication_destination)),
                ('author', models.ForeignKey(to='revuo.Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
