# greenhouse_controller.py
# NOTE:
# This Python script is a reconstructed version based on the project documentation
# and system description. The original source file was not preserved.
# Components and logic were faithfully replicated from available records.


import Adafruit_DHT
import smbus2
import RPi.GPIO as GPIO
import time
import blynklib

# Blynk auth token (replace with your actual token)
BLYNK_AUTH = 'YourBlynkAuthToken'
blynk = blynklib.Blynk(BLYNK_AUTH)

# === GPIO Pin Configuration ===
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
GY30_ADDRESS = 0x23
GY30_COMMAND = 0x20  # High-res mode

# Soil Moisture pins (BCM mode)
SOIL_PINS = [17, 27, 22, 5, 6]
RELAY_PINS = [26, 19, 13, 21, 20, 16, 12, 18]  # Exhaust fans, valves, RGB lights

# === GPIO Setup ===
GPIO.setmode(GPIO.BCM)
for pin in SOIL_PINS:
    GPIO.setup(pin, GPIO.IN)
for pin in RELAY_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)  # Default OFF

# Light Sensor Setup
bus = smbus2.SMBus(1)

# === Sensor Reading Functions ===
def read_dht():
    humidity, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return round(temp, 2), round(humidity, 2)

def read_light():
    data = bus.read_i2c_block_data(GY30_ADDRESS, GY30_COMMAND)
    light_level = (data[1] + (256 * data[0])) / 1.2
    return round(light_level, 2)

def read_soil(pin):
    return GPIO.input(pin) == 0  # 0 means wet, 1 means dry

# === Blynk Virtual Pins ===
@blynk.VIRTUAL_READ(1)
def send_temp_humidity():
    t, h = read_dht()
    blynk.virtual_write(1, t)
    blynk.virtual_write(2, h)

@blynk.VIRTUAL_READ(3)
def send_light():
    blynk.virtual_write(3, read_light())

for i, pin in enumerate(SOIL_PINS, start=4):
    @blynk.VIRTUAL_READ(i)
    def make_soil_handler(pin=pin, idx=i):
        moisture = read_soil(pin)
        blynk.virtual_write(idx, int(moisture))

# === Relay Controls ===
def control_relay(vpin, relay_index):
    @blynk.VIRTUAL_WRITE(vpin)
    def write_handler(value):
        GPIO.output(RELAY_PINS[relay_index], GPIO.LOW if int(value) == 1 else GPIO.HIGH)

# Bind relays to virtual pins 9–16
for i in range(8):
    control_relay(9 + i, i)

# === Main Loop ===
if __name__ == '__main__':
    try:
        print("Running Greenhouse IoT Controller...")
        while True:
            blynk.run()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Program stopped manually.")
    finally:
        GPIO.cleanup()
