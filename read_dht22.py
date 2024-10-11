import time
import adafruit_dht
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

DHT_SENSOR = adafruit_dht.DHT22(Pin(4))  # Use the appropriate GPIO pin number

while True:
    try:
        temperature = DHT_SENSOR.temperature
        humidity = DHT_SENSOR.humidity
        if humidity is not None and temperature is not None:
            print(f"Temp={temperature:.1f}C  Humidity={humidity:.1f}%")
        else:
            print("Failed to retrieve data from humidity sensor")
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(2)



