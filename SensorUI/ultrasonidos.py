import time
import RPi.GPIO as GPIO
import threading
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SensorUI.settings")
import django
django.setup()
from SensorApp.models import UltrasonicSensor

def main():
 # Grove - Ultrasonic Ranger connected to port D16
 sensor = GroveUltrasonicRanger(16)
 counter = 0

 t= threading.Thread(target=hombremuerto)
 t.start()

 while (hombremuerto()):
   print('se cumple')
   distance = sensor.get_distance()
   distance = (float(distance) / 100)
   print("Distance: %.2f m" % distance)
   new_sensor = UltrasonicSensor()
   new_sensor.name = "HC-SR84"
   new_sensor.description = ""
   new_sensor.pin = "16"
   new_sensor.distance = distance
   new_sensor.date = UltrasonicSensor.date
   print(str(new_sensor.date))
   new_sensor.save()
   time.sleep(4)

 estado= rangos(distance)


def hombremuerto():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(5, GPIO.IN)
  while(True):
    hombre_muerto= GPIO.input(5)
    if hombre_muerto == False:
      marca_pulsador=1
    else:
      marca_pulsador=0  
    return marca_pulsador


def rangos(distance):

  if(distance<=1.5):
    rango=1
  elif(distance>1.5 and distance<=2):
    rango=2 
  elif(distance>2):
    rango=3
  return rango




if __name__ == '__main__':
 main()
