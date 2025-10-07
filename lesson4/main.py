import network, time
from machine import Pin
import dht
import urequests

WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

WRITE_API_KEY = "JGVK0VSGAXAOOBYD"
THINGSPEAK_UPDATE_URL = "http://api.thingspeak.com/update"

sensor = dht.DHT22(Pin(15))

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Yhdistetään Wi-Fiin...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        t0 = time.time()
        while not wlan.isconnected() and time.time() - t0 < 20:
            time.sleep(0.5)
    print("Wi-Fi OK:", wlan.ifconfig() if wlan.isconnected() else "EI YHTEYTTÄ")
    return wlan.isconnected()

def send_to_thingspeak(temp, hum):
    params = f"?api_key={WRITE_API_KEY}&field1={temp:.2f}&field2={hum:.2f}"
    url = THINGSPEAK_UPDATE_URL + params
    try:
        r = urequests.get(url)
        print("ThingSpeak response:", r.text)
        r.close()
    except Exception as e:
        print("HTTP error:", e)

def read_dht():
    try:
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        print("DHT22:", t, "°C,", h, "%")
        return t, h
    except Exception as e:
        print("DHT error:", e)
        return None, None

def main():
    if not wifi_connect():
        print("Ei Wi-Fiä, yritetään silti loopata...")
    while True:
        t, h = read_dht()
        if t is not None and h is not None:
            send_to_thingspeak(t, h)
        time.sleep(20)

main()
