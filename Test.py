#!/usr/bin/env python

from MCP4728_lib import MCP4728
DAC = MCP4728()


m = 1
while True:
    i = 0
    if (m % 2) == 0:
        DAC.setVRefs(1)
        if (m % 4) == 0:
            DAC.setGain(1)
        else:
            DAC.setGain(0)
    else:
        DAC.setVRefs(0)
    while i <= 4095:
        print(i)
        DAC.setAllVoltage(i,i,i,i) 
        i += 1
    m += 1