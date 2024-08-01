# Generated by Django 5.0.7 on 2024-08-01 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=20)),
                ('screem_size', models.PositiveIntegerField(max_length=20)),
                ('available', models.BooleanField()),
                ('country', models.CharField(max_length=20)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse_module.brand')),
            ],
        ),
    ]