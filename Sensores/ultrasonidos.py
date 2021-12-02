import time
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
def main():
 # Grove - Ultrasonic Ranger connected to port D16
 sensor = GroveUltrasonicRanger(16)
 while True:
   distance = sensor.get_distance()
   print('{} cm'.format(distance))
   if distance < 100:
      print('Cerca')
   else:
      print('Lejos')
   time.sleep(1)
   
if __name__ == '__main__':
 main()