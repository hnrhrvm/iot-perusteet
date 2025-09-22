from machine import Pin
import time

led_red    = Pin(15, Pin.OUT, value=0)
led_yellow = Pin(14, Pin.OUT, value=0)
led_green  = Pin(13, Pin.OUT, value=0)
buzzer     = Pin(12, Pin.OUT, value=0)
button     = Pin(16, Pin.IN, Pin.PULL_DOWN)

GREEN_TIME = 2
YELLOW_TIME = 2
RED_TIME = 2
RED_YELLOW_TIME  = 2
STOP_EXTRA = 5
BEEP_ON  = 0.2
BEEP_OFF = 0.2

stop_request = False

def on_button(pin):
    global stop_request
    stop_request = True

button.irq(trigger=Pin.IRQ_RISING, handler=on_button)

def set_lights(red=False, yellow=False, green=False):
    led_red.value(1 if red else 0)
    led_yellow.value(1 if yellow else 0)
    led_green.value(1 if green else 0)

def beep_for(seconds):
    end_time = time.time() + seconds
    while time.time() < end_time:
        buzzer.value(1)
        time.sleep(BEEP_ON)
        buzzer.value(0)
        remaining = end_time - time.time()
        if remaining <= 0:
            break
        time.sleep(min(BEEP_OFF, remaining))

while True:
    set_lights(green=True)
    buzzer.value(0)
    time.sleep(GREEN_TIME)

    set_lights(yellow=True)
    time.sleep(YELLOW_TIME)

    set_lights(red=True)
    time.sleep(RED_TIME)

    if stop_request:
        beep_for(STOP_EXTRA)
        stop_request = False

    set_lights(red=True, yellow=True)
    time.sleep(RED_YELLOW_TIME)
