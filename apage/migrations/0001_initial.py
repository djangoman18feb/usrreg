# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-30 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_image', models.CharField(max_length=150)),
                ('artist_his', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=3000)),
                ('q_img', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='about_art',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apage.Quote'),
        ),
    ]
