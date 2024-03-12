from typing import List
import nidaqmx
import nidaqmx.system


def get_connected_devices() -> List[nidaqmx.system.Device]:
    started_devices = []
    system = nidaqmx.system.System.local()
    for device in system.devices:
        try:
            device_name = device.ai_physical_chans.channel_names[0]
            task = nidaqmx.Task()
            task.ai_channels.add_ai_voltage_chan(device_name)
            task.start()
            task.stop()
            task.close()
            started_devices.append(device)
        except:
            pass
    return started_devices
