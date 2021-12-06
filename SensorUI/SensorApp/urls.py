from django.conf.urls import url
from . import views
from .views import IndexView, SensorDetailView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('ultrasonicSensor/<int:pk>/', SensorDetailView.as_view(), name='uSensor-detail'),
] 