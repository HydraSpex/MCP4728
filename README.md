# MCP4728
This library is for the MCP4728 12-bit Quad-Digital-to-Analog Converter with EEPROM connected via I²C and its variants.<br>
Also works with the Adafruit, QITA an other brand Breakout Boards.<br>
It is designed to work on a Raspberry Pi and requires Python 3.

## Installation & Requirements
Just copy the library (MCP4728_lib.py) in your project folder.<br>
Requires "smbus". Normally preinstalled!

## Supports the major MCP4725 features:
- Fast write
- Register write
- EEPROM write
- wake up
- set Gain
- set VRef
- reset

## Usage
The values of the four outputs can be set at once or independently and can be put o EEPROM.
The values range from 0 to 4095 (12-Bit)

## Extra
In the repo you will find the datasheet for the MCP4728 series and a Test-File.
