from django.conf.urls import url
from . import views
from .views import IndexView, uSensorDetailView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('ultrasonicSensor/<int:pk>/', uSensorDetailView.as_view(), name='uSensor-detail'),
] 