# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('bio', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copy_number', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edition_number', models.CharField(max_length=20)),
                ('changes', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='edition',
            name='works',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deep.Works'),
        ),
        migrations.AddField(
            model_name='copy',
            name='edition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deep.Edition'),
        ),
        migrations.AddField(
            model_name='author',
            name='works',
            field=models.ManyToManyField(blank=True, null=True, to='deep.Works'),
        ),
    ]
