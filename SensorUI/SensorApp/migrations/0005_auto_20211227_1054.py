# Generated by Django 3.2.9 on 2021-12-27 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SensorApp', '0004_alter_ultrasonicsensor_distance'),
    ]

    operations = [
        migrations.CreateModel(
            name='UltrasonicSensorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('pin', models.IntegerField()),
                ('distance', models.DecimalField(decimal_places=4, max_digits=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UltrasonicSensorMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='HC-SR04', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='UltrasonicSensor',
        ),
        migrations.AddField(
            model_name='ultrasonicsensordetail',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SensorApp.ultrasonicsensormaster'),
        ),
    ]