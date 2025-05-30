import time
from smbus2 import SMBus
import constants

bus = SMBus(1)

def init_i2c(bus_number=1):
    global bus
    bus = SMBus(bus_number)

def write_byte(addr, value):
    try:
        bus.write_byte(addr, value)
    except Exception as e:
        print(f"I2C Write Error @ 0x{addr:02X}: {e}")

def read_byte(addr):
    try:
        return bus.read_byte(addr)
    except Exception as e:
        print(f"I2C Read Error @ 0x{addr:02X}: {e}")
        return None
