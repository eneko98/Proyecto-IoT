from django.db import models

class UltrasonicSensor(models.Model):
    """
    Ultrasonic Sensor Model
    """
    name = models.CharField(max_length=50, default="HC-SR04")
    description = models.TextField()
    pin = models.IntegerField()
    distance = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
