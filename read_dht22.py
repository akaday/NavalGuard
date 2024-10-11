import time
from gpiozero import LED, Button

led = LED(17)  # Use the appropriate GPIO pin
button = Button(2)  # Example button on GPIO pin 2

def toggle_led():
    led.toggle()
    print("LED toggled")

button.when_pressed = toggle_led

while True:
    time.sleep(1)

