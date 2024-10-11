import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # Use the appropriate GPIO pin number

def read_dht22():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(f"Temp={temperature:.1f}C  Humidity={humidity:.1f}%")
    else:
        print("Failed to retrieve data from humidity sensor")

if __name__ == "__main__":
    while True:
        read_dht22()
        time.sleep(2)

