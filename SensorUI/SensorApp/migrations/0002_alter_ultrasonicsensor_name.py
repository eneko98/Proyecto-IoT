# Generated by Django 3.2.9 on 2021-12-06 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SensorApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ultrasonicsensor',
            name='name',
            field=models.CharField(default='HC-SR04', max_length=50),
        ),
    ]
