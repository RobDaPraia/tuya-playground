'''
Playing with Tuya enabled devices to discover the DPs
Intention is to make Home Assistant plug-ins,
as the standard/generic/local tuya did not work 100%

Example Usage of TinyTuya 
https://github.com/jasonacox/tinytuya
'''

import time
import json
from AvattoThermostat import AvattoThermostat
from EuromHeater import EuromHeater

def Heater(device):  
    '''
    Eurocom Tuya Heater

    | DP ID               | Code | Type    | Values                                             |
    | ------------------- | ---- | ------- | -------------------------------------------------- |
    | Power               | 1    | Boolean | {True,False}                                       |
    | Set temperature     | 2    | Integer | {"unit":"℃","min":0,"max":37,"scale":0,"step":1}  |
    | Current temperature | 3    | Integer | {"unit":"℃","min":-9,"max":99,"scale":0,"step":1} |
    | Mode                | 4    | Enum    | ["p","m"]                                          |
    | Setting             | 101  | Enum    | ["low","mid","high","off"]                         |
    | Eco                 | 102  | Boolean | {True,False}                                       |
    | ?                   | 103  |         |                                                    |
    | Smart Timer         | 104  |         |                                                    |
    | Fault               | 12   |         |                                                    |
    '''      
 
    d = EuromHeater(device["deviceId"], device["deviceHost"], device["deviceLocalKey"])
    d.set_version(3.3)
    data = d.status() 
    print('Device: '+ device["deviceName"] + ', status: %r' % data)
   
    return 

def Thermostat(device):
    '''
    Avatto Tuya Thermostat

    | DP ID                    | Code | Type    | Values       |
    | ------------------------ | ---- | ------- | ------------ |
    | Power                    | 1    | Boolean | {True,False} |
    | Mode                     | 2    |         |              |
    | ?                        | 36   |         |              |
    | Switch Diff              | 101  |         |              |
    | Week Program             | 38   |         |              |
    | Program Mode             | 102  |         |              |
    | Restore factory settings | 39   |         |              |
    | Child lock               | 40   |         |              |
    | ?                        | 10   |         |              |
    | Sensor select            | 43   |         |              |
    | Fault alarm              | 45   |         |              |
    | Set temperature          | 16   |         |              |
    | Upper temperature limit  | 19   |         |              |
    | Current temperature      | 24   |         |              |
    | Lower temperature limit  | 26   |         |              |
    '''    
 
    d = AvattoThermostat(device["deviceId"], device["deviceHost"], device["deviceLocalKey"])
    d.set_version(3.3)
    data = d.status() 
    print('Device: '+ device["deviceName"] + ', status: %r' % data)

    temperature = d.get_room_temperature() 
    print('Device: '+ device["deviceName"] + ', temperature: %r' % temperature)

    print ('Device: '+ device["deviceName"] +' turn on')
    d.turn_on()
    time.sleep(1)

    print ('Device: '+ device["deviceName"] +' set target temperature to 17')
    d.set_target_temperature(17)
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' set target temperature to 13')
    d.set_target_temperature(13)
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' turn off')
    d.turn_off()

    return 

with open('local.settings.json', 'r') as f:
  data = json.load(f)

for device in data:
    print ('Device: '+ device["deviceName"])
    match device["deviceType"]:
        case "EuromHeater":
            Heater(device)
        case "AvattoThermostat":
            Thermostat(device)
        case _:
            print("Don't know what to do with deviceType: "+ device["deviceType"])

# return payload of devices
# Seems not working, Scan Complete!  Found 0 devices.
#devices = tinytuya.deviceScan(True)
#print('Devices found: %r' % devices)




