---
layout: post 
title: "Project Raspberry Pi Zero EDUcation"
---

Raspi startup for Education : connected traffic lights 

# Project Raspberry Pi Zero EDUcation  

    4-5 Gruppen, (Analog-Schalter, Ampel 1-4)
    5 Raspi , MicroSD-Karte , 
    5 x Stromversorgung 
    Netzterkverbindung ,
    1 WLAN - Router + IP + DHCP 
    5 x 3 LEDs (Rot / Gelb / Grün ) mit Vorwiederstand , 
    3 x 5 Verbindungskabel LED 
    5 x Schalter 

    Software:
    ISO Image Rasberian 
    ISO Image Config : + Client Wlan zum WLANRouter + SSH-Server + RDP - Server, VPN Server 
    Putty + Winscp + RDP Client / REal - VNC Client 


## SSH
  
Datei mit dem Namen "**SSH**" anlegen 

## WLAN

<https://pi-buch.info/wlan-schon-vor-der-installation-konfigurieren/>

Datei mit dem Namen "**wpa_supplicant.conf**" anlegen mit UNIX (LF) mit 

    country=DE 
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev 
    update_config=1 
    network={
         ssid="softwareengel"
         scan_ssid=1
         psk="PaSSWoRd"
         key_mgmt=WPA-PSK
    }


## ssh putty 

login: pi, pass: raspberry 

## mc

sudo apt-get install mc


## RDP 

    sudo apt-get purge realvnc-vnc-server

    sudo apt-get install xrdp

    sudo reboot

### RDP Clients 

Linux <http://www.rdesktop.org/>

Mac OS X <https://itunes.apple.com/de/app/microsoft-remote-desktop/id715768417?mt=12>

## Code 

Remote Debugging <https://www.hanselman.com/blog/RemoteDebuggingWithVSCodeOnWindowsToARaspberryPiUsingNETCoreOnARM.aspx>

### VS CODE Remote Dev Extension 

(funktioniert leider (noch ) nicht auf Raspi Zero (Arm V6)) soll März 2020 kommen 

<https://code.visualstudio.com/docs/remote/remote-overview>

<https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack>

![Remote Sev Extension](/pic/remoteSevExtension.png)

<https://github.com/microsoft/vscode-remote-release/issues/2493>

<https://github.com/microsoft/vscode-remote-release/issues/669>

### Pinbelegung 

    pinout 

![Raspi Pinbelegung](/pic/raspi-pinbelegung.png)

Interactive Pinout <https://pinout.xyz/pinout/>

## Python 2 / 3 

Nicht genutzt: python -> python 2

aktuell benutzt: python3 -> python 3 


### Python WebLed-Code 

~~~PY
    import RPi.GPIO as GPIO
    import time


    from http.server import BaseHTTPRequestHandler, HTTPServer
    import time


    print ("EDU - AMPEL") 
    print ("RPi: " , GPIO.RPI_REVISION, GPIO.RPI_INFO )
    # Webserver 



    hostName = "0.0.0.0"
    hostPort = 8000
    GPIO.setmode(GPIO.BCM) 
    isGruen = False

    def setLED (rot, gelb, gruen):
	    GPIO.setmode(GPIO.BCM) 
	    GPIO.setup(4, GPIO.OUT)
	    isGruen = gruen
	    if gruen :
		
		
		    GPIO.output (4, True)
	    else:
		    GPIO.output (4, False)
		
    class MyServer(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes('<html><head> <meta charset="UTF-8"><title>Title goes here.</title></head>', "utf-8"))
            self.wfile.write(bytes("<body><p>Webserver Response</p>", "utf-8"))
            self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        
            if ("gruen" in self.path):
                setLED(0,0,1)
                self.wfile.write(bytes("<p> %s</p>" % "Grün", "utf-8"))
            else:
                setLED(0,0,0)
                self.wfile.write(bytes("</body></html>", "utf-8"))

    myServer = HTTPServer((hostName, hostPort), MyServer)
    print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass

    myServer.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
    GPIO.cleanup()
~~~
---

![Screen Raspi Zero Webserver Led](/pic/screen-raspi-zero-webserver-led.png)

![Screen Raspi Zero Webserver Led Console](/pic/screen-raspi-zero-webserver-led-console.png)

![Screen Raspi Zero Webserver Led Thonny](/pic/screen-raspi-zero-webserver-led-thonny.png)


