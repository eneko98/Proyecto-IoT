import time
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
def main():
    sensor = GroveUltrasonicRanger(16)
    while True: #mientras no se de el paro del sistema (cambiar)
        distance = sensor.get_distance()/100
        print(distance)
        if distance < 1.50:
            print('Cerca')
        else:
            print('Lejos')
        time.sleep(1)


if __name__ == '__main__':
    main()