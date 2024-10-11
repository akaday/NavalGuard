import time
import sensor

DHT_SENSOR = sensor.DHT22(pin=4)  # Adjust pin number as needed

def read_dht22():
    try:
        result = DHT_SENSOR.read()
        if result.is_valid():
            print(f"Temp={result.temperature:.1f}C  Humidity={result.humidity:.1f}%")
        else:
            print("Failed to retrieve data from humidity sensor")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        read_dht22()
        time.sleep(2)  # Read every 2 seconds
