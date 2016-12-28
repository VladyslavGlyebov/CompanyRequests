# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activ',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cub_number', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Activs',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='LifeCycle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opened', models.DateField()),
                ('distributed', models.DateField(null=True)),
                ('proccesing', models.DateField(null=True)),
                ('checking', models.DateField(null=True)),
                ('closed', models.DateField(null=True)),
            ],
            options={
                'db_table': 'Lifecycles',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=200)),
                ('status', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('executor', models.IntegerField(null=True)),
                ('activ', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='requests.Activ')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='requests.Category')),
                ('lifecycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requests.LifeCycle')),
            ],
            options={
                'db_table': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='requests.Department')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requests.Role')),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='requests.User'),
        ),
        migrations.AddField(
            model_name='activ',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='requests.Department'),
        ),
    ]
