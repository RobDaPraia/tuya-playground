from tinytuya.core import Device

"""
 Python module to interface with Tuya Avatto Thermostat

 Local Control Classes
    AvattoThermostat(..., version=3.3)
        This class uses a default version of 3.3
        See OutletDevice() for the other constructor arguments

 Functions
    AvattoThermostat:
        status_json()
        get_room_temperature()
        get_target_temperature()
        set_target_temperature()
        get_operating_mode()
        set_operating_mode()
        get_fan_speed()
        set_fan_speed()
        get_current_state()
        get_timer()
        set_timer()
        get_temperature_unit()
        set_temperature_unit()
    Inherited
        json = status()                    # returns json payload
        set_version(version)               # 3.1 [default] or 3.3
        set_socketPersistent(False/True)   # False [default] or True
        set_socketNODELAY(False/True)      # False or True [default]
        set_socketRetryLimit(integer)      # retry count limit [default 5]
        set_socketTimeout(timeout)         # set connection timeout in seconds [default 5]
        set_dpsUsed(dps_to_request)        # add data points (DPS) to request
        add_dps_to_request(index)          # add data point (DPS) index set to None
        set_retry(retry=True)              # retry if response payload is truncated
        set_status(on, switch=1, nowait)   # Set status of switch to 'on' or 'off' (bool)
        set_value(index, value, nowait)    # Set int value of any index.
        heartbeat(nowait)                  # Send heartbeat to device
        updatedps(index=[1], nowait)       # Send updatedps command to device
        turn_on(switch=1, nowait)          # Turn on device / switch #
        turn_off(switch=1, nowait)         # Turn off
        set_timer(num_secs, nowait)        # Set timer for num_secs
        set_debug(toggle, color)           # Activate verbose debugging output
        set_sendWait(num_secs)             # Time to wait after sending commands before pulling response
        detect_available_dps()             # Return list of DPS available from device
        generate_payload(command, data)    # Generate TuyaMessage payload for command with data
        send(payload)                      # Send payload to device (do not wait for response)
        receive()
"""


class AvattoThermostat(Device):
    """
    Represents a Tuya based Avatto Thermostat
    """

    DPS_POWER = "1"
    DPS_SET_TEMP = "16"
    DPS_CUR_TEMP = "24"
  
    def __init__(self, *args, **kwargs):
        # set the default version to 3.3 as there are no 3.1 devices
        if 'version' not in kwargs or not kwargs['version']:
            kwargs['version'] = 3.3
        super(AvattoThermostat, self).__init__(*args, **kwargs)

    def status_json(self):
        """Wrapper around status() that replace DPS indices with human readable labels."""
        status = self.status()["dps"]
        return {
            "Power On": status[self.DPS_POWER],
            "Set temperature": status[self.DPS_SET_TEMP],
            "Current temperature": status[self.DPS_CUR_TEMP],
        }

    def get_room_temperature(self):
        status = self.status()["dps"]
        return status[self.DPS_CUR_TEMP]/10

    def get_target_temperature(self):
        status = self.status()["dps"]
        return status[self.DPS_SET_TEMP]

    def set_target_temperature(self, t):
        def is_float(f):
            try:
                float(f)
                return True
            except ValueError:
                return False

        # non numeric values can confuse the unit
        if not is_float(t):
            return

        self.set_value(self.DPS_SET_TEMP, t)

