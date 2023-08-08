from pydantic import BaseModel
from typing import List

class SensorData(BaseModel):
    name: str
    value: float

class DataEntry(BaseModel):
    timestamp: str
    machine_status: str
    sensors: List[SensorData]

class DataInputModel(BaseModel):
    """Request city model schema"""
    data: List[DataEntry]
