# Generated by Django 5.0.7 on 2024-08-02 20:36

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='screem_size',
            field=models.PositiveIntegerField(),
        ),
    ]
