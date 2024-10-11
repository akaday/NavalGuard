import serial
import time

ser = serial.Serial('/dev/ttyS1', 9600)  # Adjust to your COM port

def read_serial():
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(f"Serial read: {line}")

if __name__ == "__main__":
    while True:
        read_serial()
        time.sleep(2)


