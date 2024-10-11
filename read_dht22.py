import time
import adafruit_dht
import digitalio
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

dhtDevice = adafruit_dht.DHT22(Pin(4))

while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(f"Temp: {temperature:.1f}C Humidity: {humidity:.1f}%")
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(2)


