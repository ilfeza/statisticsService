from pydantic import BaseModel


class MeasureCreate(BaseModel):
    x: float
    y: float
    z: float


class StatisticValues(BaseModel):
    min: float | None
    max: float | None
    count: int
    sum: float | None
    median: float | None


class StatisticsResponse(BaseModel):
    x: StatisticValues
    y: StatisticValues
    z: StatisticValues


class DeviceCreate(BaseModel):
    id: int
    name: str
