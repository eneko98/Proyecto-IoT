from django.db import models
from decimal import Decimal

class UltrasonicSensor(models.Model):
    """
    Ultrasonic Sensor Model
    """
    name = models.CharField(max_length=50, default="HC-SR04")
    description = models.TextField()
    pin = models.IntegerField()
    distance = models.DecimalField(max_digits=20, decimal_places=4)
    date = models.DateTimeField(auto_now_add=True)
