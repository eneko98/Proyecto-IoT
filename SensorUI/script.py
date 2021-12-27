import time
from typing import Match
import RPi.GPIO as GPIO
import threading
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.display.jhd1802 import JHD1802
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

   distance = sensor.get_distance()
   distance = (float(distance) / 100)
   print("Distance: %.2f m" % distance)
   

   estado= rangos(distance)
   print(estado)
   print("\n")
   lcd_texto(estado)

   new_sensor = UltrasonicSensor()
   new_sensor.name = "HC-SR84"
   new_sensor.description = ""
   new_sensor.pin = "16"
   new_sensor.distance = distance
   new_sensor.date = UltrasonicSensor.date
   #print(str(new_sensor.date))
   new_sensor.save()
   
   time.sleep(4)


def hombremuerto():
  while(True):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN)
    hombre_muerto= GPIO.input(6)

    if hombre_muerto == False:
      print('pulsado')
      marca_pulsador=1

    else:
      print('no pulsado')
      marca_pulsador=0  
    return marca_pulsador


def rangos(distance):

  if(distance<=1.5):
    estado=1
  elif(1.5 < distance <= 2):
    estado=2 
  elif(distance>2):
    estado=3
  return estado

def lcd_texto(estado):
  lcd = JHD1802()

  if(estado==1):
   lcd.setCursor(0, 0)
   lcd.write('ALARMA')
   lcd.setCursor(1, 0)
   lcd.write('Peligro, alejese')
  elif(estado==2):
   lcd.setCursor(0, 0)
   lcd.write('WARNING')
   lcd.setCursor(0, 1)
   lcd.write('Modere la distancia')
  elif(estado==3):
   lcd.setCursor(0, 0)
   lcd.write('OK')
   lcd.setCursor(0, 1)
   lcd.write('Distancia correcta') 

if __name__ == '__main__':
 main()
