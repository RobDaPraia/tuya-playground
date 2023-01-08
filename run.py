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
    Test interaction with Eurocom Tuya Heater 
    '''      
 
    d = EuromHeater(device["deviceId"], device["deviceHost"], device["deviceLocalKey"])
    d.set_version(3.3)
    data = d.status() 
    print('Device: '+ device["deviceName"] + ', status: %r' % data)
   
    if data and "Err" in data:
        return

    data = d.status_json()
    print('Device: '+ device["deviceName"] + ', status_json: %r' % data)
   
    print ('Device: '+ device["deviceName"] +' turn on')
    d.turn_on()
    time.sleep(1)
    
    t = d.get_room_temperature()
    print ('Device: '+ device["deviceName"] +' get temperature: %.1f' % t)
  
    t = d.get_target_temperature()
    print ('Device: '+ device["deviceName"] +' get target temperature: %.1f' % t)
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' set target temperature to 17')
    d.set_target_temperature(17)
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' set target temperature to 13')
    d.set_target_temperature(13)
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' set mode to manual')
    d.set_operating_mode("m")
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' set mode to automatic')
    d.set_operating_mode("p")
    time.sleep(5)   

    print ('Device: '+ device["deviceName"] +' set setting to high')
    d.set_setting("high")
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' set setting to mid')
    d.set_setting("mid")
    time.sleep(5)
    
    print ('Device: '+ device["deviceName"] +' set setting to low')
    d.set_setting("low")
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' set setting to off')
    d.set_setting("off")
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' set mode to automatic')
    d.set_operating_mode("p")
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' turn ECO mode on')
    d.eco_on()
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' turn ECO mode off')
    d.eco_off()
    time.sleep(5)

    print ('Device: '+ device["deviceName"] +' turn off')
    d.turn_off()
    
    return 

def Thermostat(device):
    '''
    Test interaction with Avatto Tuya Thermostat 
    '''    
 
    d = AvattoThermostat(device["deviceId"], device["deviceHost"], device["deviceLocalKey"])
    d.set_version(3.3)
    data = d.status() 
    print('Device: '+ device["deviceName"] + ', status: %r' % data)
    
    if data and "Err" in data:
        return

    data = d.status_json()
    print('Device: '+ device["deviceName"] + ', status_json: %r' % data)
   
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




