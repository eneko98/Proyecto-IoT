# Generated by Django 3.2.10 on 2022-01-02 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SensorApp', '0012_auto_20211230_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='lcdsensor',
            name='okMessage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='camerasensor',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='lcdsensor',
            name='emergencyMessage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lcdsensor',
            name='name',
            field=models.CharField(default='JHD1802', max_length=100),
        ),
        migrations.AlterField(
            model_name='lcdsensor',
            name='stopMessage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
