import serial
import requests

openhab_host = '127.0.0.1'
openhab_port = '8080'

def send_status_to_openhab(key, value, station):
  url = 'http://{host}:{port}/rest/items/Arduino_{station}{key}/state'.format(host=openhab_host, port=openhab_port, station=station, key=key)
  print url
  print value

  response = requests.put(url, headers={'Content-Type': 'text/plain'}, data=str(value))
  print response 
  print response.text

  if response.status_code != requests.codes.ok:
    response.raise_for_status()     

def listen_for_data():
  ser = serial.Serial('/dev/ttyUSB0', 115200)
  while True:
    try: 
      line = ser.readline().strip()
      line = line[:-1]
      print line
      if line.startswith('R>'):
        line = line.replace('R>', '')
        station = line.split(':')[0]
        print "station = {station}".format(station=station)
        line = line.replace(station + ':', '')
        parts = line.split(';')
        for p in parts:
          key,val = p.split('=')
 	  val=val
          print "Key = '{key}', value='{val}'".format(key=key,val=val)
          send_status_to_openhab(key=key, value=val, station=station)
          #send_status_to_openhab(key=key, value="1", station=station)
    except Exception, e:
      print e
      #raise

listen_for_data()
