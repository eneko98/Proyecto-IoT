from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('camera/', views.camResultados, name='camera'),
    path('ultrasonic/', views.ultraResultados, name='ultrasonic'),
    path('lcd/', views.lcdResultados, name='lcd'),
    path('live/', views.live, name='live'),
]