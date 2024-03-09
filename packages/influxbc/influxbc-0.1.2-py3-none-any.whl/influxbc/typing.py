from typing import Union

from . import InfluxDBV1Client, InfluxDBV2Client

Client = Union[InfluxDBV1Client, InfluxDBV2Client]
