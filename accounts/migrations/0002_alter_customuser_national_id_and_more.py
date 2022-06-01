# Generated by Django 4.0.4 on 2022-06-01 20:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='national_id',
            field=models.CharField(max_length=14, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator('\\d{14}', 'Please enter a valid 14 numbers ID ')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('01\\d{9}', 'Please enter a valid Phone number')]),
        ),
    ]