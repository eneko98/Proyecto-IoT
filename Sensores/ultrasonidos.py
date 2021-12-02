import time
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
def main():
 # Grove - Ultrasonic Ranger connected to port D16
 sensor = GroveUltrasonicRanger(16)
 while True:
   distance = sensor.get_distance()
   distance = (float(distance) / 100)
   print('{:.4f} m'.format(distance))
   if distance < 1:
      print('Cerca')
   elif 1 <= distance <= 1.5:
      print('Medio')
   else:
      print('Lejos')
   time.sleep(1)
   
if __name__ == '__main__':
 main()