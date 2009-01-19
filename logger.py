#!/usr/bin/env python

import serial
from datetime import datetime
import time
import csv

t0 = datetime.now()

ser = serial.Serial('/dev/ttyUSB0', 9600)
log = csv.writer(open("log.csv", "wb"), dialect='excel')

while True:
    ser.write('A\r\n')
    motionPercent = ser.readline()
    t = datetime.now()
    log.writerow([t.strftime("%Y.%m.%d %H:%M"), motionPercent]) 
    print '%s, %s' % (t.strftime("%Y.%m.%d %H:%M"),    
                      motionPercent)        
    time.sleep(360)

# TODO: need to actually close serial port on Ctrl-C
ser.close()