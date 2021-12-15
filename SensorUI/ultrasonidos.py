import time
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SensorUI.settings")
import django
django.setup()
from SensorApp.models import UltrasonicSensor
def main():
 # Grove - Ultrasonic Ranger connected to port D16
 sensor = GroveUltrasonicRanger(16)
 counter = 10
 while (counter < 10):
   distance = sensor.get_distance()
   print("Distance: %.2f cm" % distance)
   distance = (float(distance) / 100)
   new_sensor = UltrasonicSensor()
   new_sensor.name = "HC-SR04"
   new_sensor.description = ""
   new_sensor.pin = "16"
   new_sensor.distance = distance
   new_sensor.save()
   print(new_sensor)
   time.sleep(4)
   counter = counter + 1
   
if __name__ == '__main__':
 main()