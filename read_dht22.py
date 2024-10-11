from gpiozero import LED
from time import sleep

led = LED(17)  # Use the appropriate GPIO pin number

while True:
    led.on()
    print("LED on")
    sleep(1)
    led.off()
    print("LED off")
    sleep(1)
