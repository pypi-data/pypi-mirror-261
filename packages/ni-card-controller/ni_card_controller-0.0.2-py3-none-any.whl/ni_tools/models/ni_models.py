from pydantic import BaseModel


class NIInfoModel(BaseModel):
    device: str
    product_type: str
    ai_channels: list[str]
    ao_channels: list[str]
    di_channels: list[str]
    do_channels: list[str]
    counter_channels: list[str]
    timer_channels: list[str]
    ao_max_rate_hz: float
    ai_max_single_chan_rate_hz: float
    ai_max_multi_chan_rate_hz: float
