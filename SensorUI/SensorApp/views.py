from django.http import request
from django.shortcuts import render
from .models import UltrasonicSensor, CameraSensor

def index(request):
    return render(request, "index.html")

def ultraResultados(request):
    ultraDatos = UltrasonicSensor.objects.all()
    return render(request, "sonicResultados.html", {"datos" : ultraDatos})

def camResultados(request):
    camDatos = CameraSensor.objects.all()
    return render(request, "camResultados.html", {"datos" : camDatos})

def soonResultados(request):
    """Para el siguiente sensor"""
    ultraDatos = UltrasonicSensor.objects.all()
    return render(request, "soonResultados.html", {"datos" : ultraDatos})