import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

def read_ds18b20():
    temperature = sensor.get_temperature()
    print(f"Temperature: {temperature:.2f}C")

if __name__ == "__main__":
    while True:
        read_ds18b20()
        time.sleep(2)
