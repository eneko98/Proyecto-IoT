from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import UltrasonicSensor
from Sensores import ultrasonidos

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'sensors'

    def get_queryset(self):
        return UltrasonicSensor.objects.order_by('-id')[:5]

class SensorDetailView(DetailView):
    template_name = 'sensor_detail.html'
    context_object_name = 'sensor'