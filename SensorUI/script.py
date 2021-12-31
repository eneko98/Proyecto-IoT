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
from SensorApp.models import UltrasonicSensor

#LCD TEXTO
lcd = JHD1802()
#ULTRASONIDOS
sensor = GroveUltrasonicRanger(16)
#lcd_rgb = JHD1313()

#LCD RGB
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
 colores_rgb(255,255,255)
 time.sleep(5)
 estado_anterior=1
 """t_hombremuerto= threading.Thread(target=hombremuerto)
 t_hombremuerto.start()"""
 

 #t_rearme= threading.Thread(target=boton_rearme)
 #t_rearme.start()
 #ttt = Thread(target=lambda: thistaginsert(tag))

 """t_distancia= threading.Thread(target=get_distancia)
 t_distancia.start()

 distancia_sensor = get_distancia()"""

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(26, GPIO.IN)
 salir= GPIO.input(26) 

 while(salir==0):
  
  salir= GPIO.input(26) 
  rearmado= boton_rearme(estado_anterior)
  
  if (hombremuerto() and rearmado==1):

   medida_distancia = sensor.get_distance()
   medida_distancia = (float(medida_distancia) / 100)

   print("Distance: %.2f m" % medida_distancia)
   
   if(medida_distancia<1.0):
     print('ERROR, DEMASIADO CERCA')
     rearmado=0

   estado= rangos(medida_distancia)
   print(estado)
   print("\n")
   lcds(estado)

   new_sensor = UltrasonicSensor()
   new_sensor.name = "HC-SR04"
   new_sensor.description = ""
   new_sensor.pin = "16"
   new_sensor.distance = medida_distancia
   new_sensor.date = UltrasonicSensor.date
   new_sensor.save()
   
   time.sleep(4)

  if(hombremuerto()==0 or rearmado==0):
   #rearmado=0
   time.sleep(1)
   lcd.clear()
   lcd.setCursor(0, 0)
   lcd.write('PARADA DE')
   lcd.setCursor(1, 0)
   lcd.write('EMERGENCIA')
   colores_rgb(255,0,0)
   #rearmado=0
   print('alejese y rearme el sistema')
    #rearme=0"""

  estado_anterior=rearmado

lcd.clear()

#############################################################################################
def hombremuerto():
  while(True):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.IN)
    hombre_muerto= GPIO.input(5)

    if hombre_muerto == True:
      print('pulsado')
      marca_pulsador=1

    else:
      print('no pulsado')
      marca_pulsador=0  
    return marca_pulsador

"""def get_distancia():
  while(True):    
   medida_distancia = sensor.get_distance()
   medida_distancia = (float(medida_distancia) / 100)
   print("Distance: %.2f m" % medida_distancia)
   return(medida_distancia)"""

######################################################################################
def rangos(distance):

  if(distance<=1.5):
    estado=1
  elif(1.5 < distance <= 2.3):
    estado=2 
  elif(distance>2.3):
    estado=3
  return estado

#############################################################################################
def lcds(estado):
  
  if(estado==1):
   lcd.clear()
   lcd.setCursor(0, 0)
   lcd.write('ALARMA')
   lcd.setCursor(1, 0)
   lcd.write('Peligro, alejese')
   colores_rgb(255,0,0)

  elif(estado==2):
   lcd.clear()
   lcd.setCursor(0, 0)
   lcd.write('WARNING')
   lcd.setCursor(1, 0)
   lcd.write('Modere la distancia')
   colores_rgb(255,173,0)

  elif(estado==3):
   lcd.clear()
   lcd.setCursor(0, 0)
   lcd.write('OK')
   lcd.setCursor(1, 0)
   lcd.write('Distancia OK')
   colores_rgb(0,255,0) 


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
  GPIO.setup(19, GPIO.IN)
  marca_rearme= GPIO.input(19)
  if(marca_rearme==1):
    print('rearme')
    return_rearmado=1
  else:
    return_rearmado= estado_anterior
    """print('entrado')
    marca_rearme= GPIO.input(19)

    if(marca_rearme==1 and estado_anterior==0):
      return_rearmado=1
      print('rearmado')
    elif(marca_rearme==1 and estado_anterior==1):
      return_rearmado=0
      print('desarmado')
    elif(marca_rearme==0 and estado_anterior==1):
      print('rearmadox2')
      return_rearmado=1
    else:
      print('desarmado, debes rearmar')
      return_rearmado=0"""""
    return return_rearmado

######################################################################################################
if __name__ == '__main__':
 main()
