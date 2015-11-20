== Arduino 433MHZ to OpenHAB

receiver_sensor_stations.ino
* runs on arduino
* listens for incoming messages on 433MHz (VirtualWire library)
* sends to serial port

recv_and_post_to_openhab.py
* Listens for messages on serial port  (of laptop or raspberry pi)
* Sends to openhab (on localhost)


Station names on 433MHZ need to map to "items" in openhab. Prepend "Arduino_"

e.g. 
  Station "kitchen", with a temp reading Needs an openHab item called:
  Arduino_kitchentemp

