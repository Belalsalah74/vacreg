# Generated by Django 4.0.4 on 2022-05-31 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vac', '0004_alter_vaccineshot_shot_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccineshot',
            name='register_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vaccineshot',
            name='shot_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
