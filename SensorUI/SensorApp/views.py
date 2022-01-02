from django.http import request
from django.http.response import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators import gzip
from django.views.decorators.gzip import gzip_page
from .models import UltrasonicSensor, CameraSensor, lcdSensor
from SensorApp.face_detection import VideoCamera
import cv2
import threading


def index(request):
    return render(request, "index.html")

def ultraResultados(request):
    ultraDatos = UltrasonicSensor.objects.all()
    return render(request, "sonicResultados.html", {"datos" : ultraDatos})

def camResultados(request):
    camDatos = CameraSensor.objects.all()
    return render(request, "camResultados.html", {"datos" : camDatos})

def lcdResultados(request):
    lcdDatos = lcdSensor.objects.all()
    return render(request, "lcdResultados.html", {"datos" : lcdDatos})

@gzip.gzip_page
def live(request):
    return StreamingHttpResponse(gen(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")
    
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


