from django.http import request
from django.shortcuts import render
from .models import UltrasonicSensor

class IndexView(request):
    template_name = 'index.html'
    context_object_name = 'sensors'

    def get_queryset(self):
        return UltrasonicSensor.objects.all()

class uSensorDetailView(request):
    template_name = 'sensor_detail.html'
    context_object_name = 'sensor'

    def get_queryset(self):
        return UltrasonicSensor.objects.all()