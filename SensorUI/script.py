import time,sys
from typing import Match
import RPi.GPIO as GPIO
import threading
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.display.jhd1802 import JHD1802

#from grove.display.jhd1313 import JHD1313
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SensorUI.settings")
import django
django.setup()
from SensorApp.models import UltrasonicSensor, lcdSensor

#LCD TEXTO
lcd = JHD1802()
#ULTRASONIDOS
sensor = GroveUltrasonicRanger(16)


if sys.platform == 'uwp':
    import winrt_smbus as smbus
    bus = smbus.SMBus(2)
else:
    import smbus
    rev = GPIO.RPI_REVISION
    if rev == 2 or rev == 3:
        bus = smbus.SMBus(1)
    else:
        bus = smbus.SMBus(0)
DISPLAY_RGB_ADDR = 0x62



def main():

 lcd.setCursor(1, 0)
 lcd.write('Iniciando...')
 colores_rgb(163,236,253)
 time.sleep(5)
 estado_anterior=1
 rearmado=1

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(26, GPIO.IN)
 salir= GPIO.input(26) 

 while(salir==0):
  
  estado_anterior=rearmado
  
  salir= GPIO.input(26) 
  rearmado= boton_rearme(estado_anterior)
  
  if (hombremuerto() and rearmado==1):
   servomotor()
   buzzer_sonido(0)
   medida_distancia = sensor.get_distance()
   medida_distancia = (float(medida_distancia) / 100)

   print("Distancia a la que se encuentra: %.2f m" % medida_distancia)
   
   if(medida_distancia<1.0):
     print('ERROR, DEMASIADO CERCA')
     rearmado=0

   estado= rangos(medida_distancia, rearmado)
   
   lcds(estado)

   new_Usensor = UltrasonicSensor()
   new_Usensor.name = "HC-SR04"
   new_Usensor.description = ""
   new_Usensor.pin = "16"
   new_Usensor.distance = medida_distancia
   new_Usensor.date = UltrasonicSensor.date
   new_Usensor.save()
   
   time.sleep(3)

  if(hombremuerto()==0 or rearmado==0):
   contador= contador+1

   buzzer_sonido(contador)
   new_lcdSensor = lcdSensor()
  
   rearmado=0

    
   if(rearmado==0):
    print('Rearme el sistema para continuar')

   buzzer_sonido(1)

  print('----------------------------------------------------')
 lcd.clear()
 print('EXIT...') 


#############################################################################################
def hombremuerto():
  
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(5, GPIO.IN)
  hombre_muerto= GPIO.input(5)

  if hombre_muerto == True:
    marca_pulsador=1
  else:
    print('Has soltado el hombre muerto')
    marca_pulsador=0  
  return marca_pulsador


######################################################################################
def rangos(distance, rearme_ok):

  if(distance<=1.5):
    estado=1
  elif(1.5 < distance <= 2.3):
    estado=2 
  elif(distance>2.3):
    estado=3

  if (rearme_ok==0):
    estado=4

  return estado

#############################################################################################
def lcds(estado):
  
  if(estado==1):
   new_lcdSensor=lcdSensor()
   lcd.clear()
   lcd.setCursor(0, 0)
   alarma1 = lcd.write('ALARMA')
   lcd.setCursor(1, 0)
   alarma2 = lcd.write('Peligro, alejese')
   colores_rgb(255,0,0)

   new_lcdSensor.name = "JHD1802"
   new_lcdSensor.description = ""
   new_lcdSensor.pin = "SCL,SDA"
   new_lcdSensor.date = lcdSensor.date
   new_lcdSensor.stopMessage = alarma1 + "- " + alarma2
   new_lcdSensor.save() 

  elif(estado==2):
   new_lcdSensor = lcdSensor()
   lcd.clear()
   lcd.setCursor(0, 0)
   warning1 = lcd.write('WARNING')
   lcd.setCursor(1, 0)
   warning2 = lcd.write('Modere la distancia')
   colores_rgb(255,173,0)

   new_lcdSensor.name = "JHD1802"
   new_lcdSensor.description = ""
   new_lcdSensor.pin = "SCL,SDA"
   new_lcdSensor.date = lcdSensor.date
   new_lcdSensor.warningMessage = warning1 + "- " + warning2
   new_lcdSensor.save()

  elif(estado==3):
   new_lcdSensor = lcdSensor()
   lcd.clear()
   lcd.setCursor(0, 0)
   ok1 = lcd.write('OK')
   lcd.setCursor(1, 0)
   ok2 = lcd.write('Distancia OK')
   colores_rgb(0,255,0)
   
   new_lcdSensor.name = "JHD1802"
   new_lcdSensor.description = ""
   new_lcdSensor.pin = "SCL,SDA"
   new_lcdSensor.date = lcdSensor.date
   new_lcdSensor.okMessage = ok1 + "- " + ok2
   new_lcdSensor.save()

  elif(estado==4):
   new_lcdSensor=lcdSensor()
   time.sleep(1)
   lcd.clear()
   lcd.setCursor(0, 0)
   emergency1 = lcd.write('PARADA DE')
   lcd.setCursor(1, 0)
   emergency2 = lcd.write('EMERGENCIA')
   colores_rgb(255,0,0)
   new_lcdSensor.name = "JHD1802"
   new_lcdSensor.description = ""
   new_lcdSensor.pin = "SCL,SDA"
   new_lcdSensor.date = lcdSensor.date
   new_lcdSensor.emergencyMessage = emergency1 + " " + emergency2
   new_lcdSensor.save() 


def colores_rgb(r,g,b):
    bus.write_byte_data(DISPLAY_RGB_ADDR,0,0)
    bus.write_byte_data(DISPLAY_RGB_ADDR,1,0)
    bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
    bus.write_byte_data(DISPLAY_RGB_ADDR,4,r)
    bus.write_byte_data(DISPLAY_RGB_ADDR,3,g)
    bus.write_byte_data(DISPLAY_RGB_ADDR,2,b)

#######################################################################################################
def boton_rearme(estado_anterior):

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(23, GPIO.IN)
  marca_rearme= GPIO.input(23)
  if(marca_rearme==1):
    print('Sistema rearmado')
    return_rearmado=1
  else:
    return_rearmado= estado_anterior
  return return_rearmado

def buzzer_sonido (activado):
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(22, GPIO.OUT)
  GPIO.output(22, activado)

def servomotor():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(12, GPIO.OUT)
  p = GPIO.PWM(12, 50) # GPIO 17 for PWM with 50Hz
  p.start(0)

  p.ChangeDutyCycle(2.5)
  time.sleep(0.5)
  p.ChangeDutyCycle(5)
  time.sleep(0.5)
  p.ChangeDutyCycle(7.5)
  time.sleep(0.5)
  p.ChangeDutyCycle(10)
  time.sleep(0.5)
  p.ChangeDutyCycle(12.5)
  time.sleep(0.5)
  p.ChangeDutyCycle(10)
  time.sleep(0.5)
  p.ChangeDutyCycle(7.5)
  time.sleep(0.5)
  p.ChangeDutyCycle(5)
  time.sleep(0.5)
  p.ChangeDutyCycle(2.5)
  time.sleep(0.5)

######################################################################################################
if __name__ == '__main__':
 main()
