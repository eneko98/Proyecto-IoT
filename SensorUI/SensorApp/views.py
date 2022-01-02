from django.http import request
from django.http.response import StreamingHttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators import gzip
from django.views.decorators.gzip import gzip_page
from .models import UltrasonicSensor, CameraSensor, lcdSensor
from .forms import CreateUserForm
from SensorApp.face_detection import VideoCamera
import cv2
import threading

def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    else: 
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, "User " + username + " was created successfully")
                return redirect("login")
        context = {'form': form}
        return render(request, "register.html", context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.info(request, "Username or password is incorrect")
        context = {}
        return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def index(request):
    return render(request, "index.html")

@login_required(login_url='login')
def ultraResultados(request):
    ultraDatos = UltrasonicSensor.objects.all()
    return render(request, "sonicResultados.html", {"datos" : ultraDatos})

@login_required(login_url='login')
def camResultados(request):
    camDatos = CameraSensor.objects.all()
    return render(request, "camResultados.html", {"datos" : camDatos})

@login_required(login_url='login')
def lcdResultados(request):
    lcdDatos = lcdSensor.objects.all()
    return render(request, "lcdResultados.html", {"datos" : lcdDatos})

@login_required(login_url='login')
@gzip.gzip_page
def live(request):
    return StreamingHttpResponse(gen(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")
    
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


