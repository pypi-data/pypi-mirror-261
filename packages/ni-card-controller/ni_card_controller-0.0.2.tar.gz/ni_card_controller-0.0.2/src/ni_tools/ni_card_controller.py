from typing import Optional
import logging
from ni_tools.get_connected_devices import get_connected_devices
from ni_tools.models.ni_models import NIInfoModel


class NiCardTools:
    def __init__(self, device_name: Optional[str] = None):
        _devices = get_connected_devices()
        self.device = None
        if not _devices or len(_devices) == 0:
            raise Exception("No devices connected.")
        if device_name:
            self.device = next(
                (device for device in _devices if device.name == device_name), None
            )
            if self.device is None:
                raise Exception(f"Device {device_name} not found.")
        else:
            self.device = _devices[0]
            if len(_devices) > 1:
                logging.warning(
                    "Multiple devices found. It's recommended to explicitly select the device."
                )
        self.set_device_specs()

    def set_device_specs(self) -> dict:
        self.device_info = NIInfoModel(
            device=self.device.name,
            product_type=self.device.product_type,
            ai_channels=[channel.name for channel in self.device.ai_physical_chans],
            ao_channels=[channel.name for channel in self.device.ao_physical_chans],
            di_channels=[channel.name for channel in self.device.di_lines],
            do_channels=[channel.name for channel in self.device.do_lines],
            counter_channels=[
                channel.name for channel in self.device.co_physical_chans
            ],
            timer_channels=[channel.name for channel in self.device.ci_physical_chans],
            ao_max_rate_hz=self.device.ao_max_rate,
            ai_max_single_chan_rate_hz=self.device.ai_max_single_chan_rate,
            ai_max_multi_chan_rate_hz=self.device.ai_max_multi_chan_rate,
        )
