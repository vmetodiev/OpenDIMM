#!/usr/bin/python3

#
# Within th programmer project, compile and use it as follows:
# # # cd /home/pi/ddr4s/fw/Pi
# # # ./spd_prog
# # # ./calc -f mySPD.bin
#

#
# ls /home/pi/ddr4s/spd/DDR4\ UDIMM/Corsair/40G057A.bin
# ./calc -f /home/pi/ddr4s/spd/DDR4\ UDIMM/Corsair/40G057A.bin
# 


#
# ls /home/pi/ddr4s/spd/DDR4\ UDIMM/Corsair/40G062A.bin
# ./calc -f /home/pi/ddr4s/spd/DDR4\ UDIMM/Corsair/40G062A.bin
# 

import time
import RPi.GPIO as gpio

spd_en = 16

gpio.setmode(gpio.BCM)
gpio.setup(spd_en, gpio.OUT)

time.sleep(1)

gpio.output(spd_en, gpio.HIGH)