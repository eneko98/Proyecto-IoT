#!/usr/bin/env python
 
import time
 
from grove.display.jhd1802 import JHD1802
 
def main():
    # Grove - 16x2 LCD(White on Blue) connected to I2C port
    lcd = JHD1802()
    
    while(1):

        lcd.setCursor(0, 0)
        lcd.write('hello, world!!!')

        print('application exiting...')
        lcd.clear()
        lcd.write('prueba')
    
if __name__ == '__main__':
    main()