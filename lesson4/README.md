IoT pipeline – DHT22 + Raspberry Pi Pico W + ThingSpeak

Tässä projektissa rakennettiin yksinkertainen IoT-pipeline. Raspberry Pi Pico W lukee DHT22-sensorin lämpötila- ja kosteusdataa ja lähettää sen ThingSpeakiin. Data haetaan ThingSpeakin API:sta ja näytetään graafina yksinkertaisella HTML-sivulla. Lisäksi käytettiin webhookia, joka lähettää hälytyksen, jos lämpötila ylittää asetetun rajan.

Arkkitehtuuri:
- DHT22
- Pi Pico W (Wokwi, MicroPython)
- ThingSpeak (REST API)
- Dashboard (HTML ja Chart.js)
- Webhook (React ja ThingHTTP)

Käytetyt osat:
- Raspberry Pi Pico W (Wokwi)
- DHT22-anturi
- MicroPython
- ThingSpeak
- Chart.js
- Webhook.site tai ThingHTTP

Toiminta:
- Pico W lukee DHT22:n arvot noin 20 sekunnin välein
- Arvot lähetetään ThingSpeakiin kenttiin (field1 = lämpötila, field2 = kosteus)
- Dashboard hakee datan ThingSpeakin API:sta ja piirtää sen kaaviona
- Webhook laukeaa, kun lämpötila ylittää määritetyn raja-arvon

Projektin rakenne:
- main.py  laitekoodi, joka lähettää dataa ThingSpeakiin
- diagram.json  Wokwi-simulaation kytkennät
- dashboard.html  graafi ThingSpeakin datasta
- README.md  tämä tiedosto

Yhteenveto:
- Projektissa toteutettiin koko IoT-pipeline anturilta pilvipalveluun ja graafiseen näkymään
- Toteutus toimii ilman omaa palvelinta, pelkästään Wokwi-simulaattorilla ja ThingSpeakillä
