# Generated by Django 3.1 on 2022-06-29 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_coachingstaff_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachingstaff',
            name='rol',
            field=models.CharField(choices=[('1', 'técnico'), ('2', 'asistente'), ('3', 'médico'), ('4', 'preparador')], max_length=250),
        ),
        migrations.DeleteModel(
            name='RolStaff',
        ),
    ]