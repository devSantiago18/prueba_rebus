# Generated by Django 3.1 on 2022-06-29 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20220628_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='url_shield',
            field=models.ImageField(upload_to='img/shields'),
        ),
    ]
