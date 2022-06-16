import time
import smbus
import sys
import os
import subprocess
from smbus import SMBus
from sys import exit

bus = SMBus(1)

channel0 = 0xB0
channel1 = 0xB8
channel2 = 0xB1
channel3 = 0xB9
channel4 = 0xB2
channel5 = 0xBA
channel6 = 0xB3
channel7 = 0xBB
channel8 = 0xB4
channel9 = 0xBC
channel10 = 0xB5
channel11 = 0xBD
channel12 = 0xB6
channel13 = 0xBE
channel14 = 0xB7
channel15 = 0xBF

address = 0b1110110

vref = 3.3
lange = 0x06
zeit = 5
tiempo = 0.3
max_reading = 8388608.0


def getReading(adc_address, adc_channel):
    bus.write_byte(adc_address, adc_channel)
    time.sleep(tiempo)
    reading = bus.read_i2c_block_data(adc_address, adc_channel, lange)
    value = ((((reading[0]&0x3F))<<16))+((reading[1]<<8))+(((reading[2]&0xE0)))
    volt = value * vref/max_reading
    return volt
    
time.sleep(tiempo)

ch0_mult = 1
ch1_mult = 1

while(True):
    Ch0Value = ch0_mult*getReading(address, channel0)
    print("Channel 0 Reading: %12.2f V" % (Ch0Value))
    time.sleep(tiempo)
    Ch1Value = ch1_mult*getReading(address, channel1)
    print("Channel 1 Reading: %12.2f V" % (Ch1Value))
    time.sleep(tiempo)
    sys.stdout.flush


    



 