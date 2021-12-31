from django.db import models
from decimal import Decimal


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    pin = models.IntegerField()

    class Meta:
        abstract = True

class UltrasonicSensor(Sensor):
    """
    Ultrasonic Sensor Model
    """
    name = models.CharField(max_length=100, default="HC-SR04")
    distance = models.DecimalField(max_digits=20, decimal_places=4)

class CameraSensor(Sensor):
    """
    Camera Sensor Model
    """
    imagen = models.ImageField(upload_to='media/', null=True, blank=True)
    
class lcdSensor(Sensor):
    """
    lcd Sensor Model
    """
    name = models.CharField(max_length=100, default="Grove LCD BoW")
    stopMessage = models.CharField(max_length=255)
    emergencyMessage = models.CharField(max_length=255)