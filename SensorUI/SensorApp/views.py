from django.http import request
from django.shortcuts import render
from .models import UltrasonicSensor, CameraSensor, lcdSensor

def index(request):
    return render(request, "index.html")

def ultraResultados(request):
    ultraDatos = UltrasonicSensor.objects.all()
    return render(request, "sonicResultados.html", {"datos" : ultraDatos})

def camResultados(request):
    camDatos = CameraSensor.objects.all()
    return render(request, "camResultados.html", {"datos" : camDatos})

def lcdResultados(request):
    """Para el siguiente sensor"""
    lcdDatos = lcdSensor.objects.all()
    return render(request, "lcdResultados.html", {"datos" : lcdDatos})