from machine import Pin
import utime

pir = Pin(28, Pin.IN, Pin.PULL_DOWN)
led = Pin("LED", Pin.OUT)

while True:
    if pir.value():
        print("Motion detected!")
        for _ in range(3):
            led.value(1)
            utime.sleep_ms(200)
            led.value(0)
            utime.sleep_ms(200)
        while pir.value():
            utime.sleep_ms(100)
    else:
        utime.sleep_ms(100)
