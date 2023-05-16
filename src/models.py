from typing import Tuple, List
from pydantic import BaseModel

class Device(BaseModel):
    name: str
    description: str


class MeasurementMeta(BaseModel):
    id: int
    device_id: int

class MeasurementData(BaseModel):
    meta: MeasurementMeta
    data: List[Tuple[float, float]]