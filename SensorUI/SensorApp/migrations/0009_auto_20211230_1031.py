# Generated by Django 3.2.9 on 2021-12-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SensorApp', '0008_lcdsensor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ultrasonicsensor',
            name='name',
        ),
        migrations.AlterField(
            model_name='lcdsensor',
            name='name',
            field=models.CharField(default='Grove LCD BoW', max_length=100),
        ),
    ]
