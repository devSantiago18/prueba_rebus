# Generated by Django 3.1 on 2022-06-29 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20220629_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img_flag',
            field=models.ImageField(blank=True, null=True, upload_to='img/flags'),
        ),
    ]
