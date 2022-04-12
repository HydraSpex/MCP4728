import smbus

DAC_ADDRESS = 0x60

WRITEDAC            = 0x50
WRITEDACEEPROMCH0   = 0x58
WRITEDACEEPROMCH1   = 0X5A
WRITEDACEEPROMCH2   = 0X5C
WRITEDACEEPROMCH3   = 0X5E

GENERAL_CALL_ADDRESS = 0x00
GENERAL_CALL_RESET_COMMAND = 0x06
GENERAL_CALL_WAKEUP_COMMAND = 0x09

class MCP4728(object):
    def __init__(self, address = DAC_ADDRESS, busnum = 1):
        self.address = address
        self.bus = smbus.SMBus(busnum)
        
    def setAllVoltage(self, volt0, volt1, volt2, volt3):
        if (volt0 > 4095):
            volt0 = 4095
        if (volt0 < 0):
            volt0 = 0
        if (volt1 > 4095):
            volt1 = 4095
        if (volt1 < 0):
            volt1 = 0
        if (volt2 > 4095):
            volt2 = 4095
        if (volt2 < 0):
            volt2 = 0
        if (volt3 > 4095):
            volt3 = 4095
        if (volt3 < 0):
            volt3 = 0
            
        val = [(volt0 >> 8) & 0xFF, (volt0) & 0xFF, (volt1 >> 8) & 0xFF, (volt1) & 0xFF, (volt2 >> 8) & 0xFF, (volt2) & 0xFF, (volt3 >> 8) & 0xFF, (volt3) & 0xFF]    
        try:
            self.bus.write_i2c_block_data(self.address, WRITEDAC, val)
        except:
            pass

    def setOneVoltage(self, CH, volt):
        val = [(volt >> 8) & 0xFF, (volt) & 0xFF]
        if CH == 0:
            try:
                self.bus.write_i2c_block_data(self.address, WRITEDACEEPROMCH0, val)
            except:
                pass
        elif CH == 1:
            try:
                self.bus.write_i2c_block_data(self.address, WRITEDACEEPROMCH1, val)
            except:
                pass
        elif CH == 2:
            try:
                self.bus.write_i2c_block_data(self.address, WRITEDACEEPROMCH2, val)
            except:
                pass
        elif CH == 3:
            try:
                self.bus.write_i2c_block_data(self.address, WRITEDACEEPROMCH3, val)
            except:
                pass
        else:
            print("Wrong Channel")

    def setVRefs(self, vref):
        if vref == 0 or vref == 1:
            gain_command = 0b10000000
            gain_command |= vref << 3
            gain_command |= vref << 2
            gain_command |= vref << 1
            gain_command |= vref
            self.bus.write_i2c_block_data(self.address, 0, gain_command)
        else:
            pass

    def setGains(self, gain):
        if gain == 0 or gain == 1:
            sync_command = 0b11000000
            sync_command |= gain << 3
            sync_command |= gain << 2
            sync_command |= gain << 1
            sync_command |= gain
            self.bus.write_i2c_block_data(self.address, 0, sync_command)
        else:
            pass

    def reset(self):
        self.bus.write_i2c_block_data(self.address, GENERAL_CALL_ADDRESS, GENERAL_CALL_RESET_COMMAND)

    def wakeup(self):
        self.bus.write_i2c_block_data(self.address, GENERAL_CALL_ADDRESS, GENERAL_CALL_WAKEUP_COMMAND)