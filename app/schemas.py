from typing import List

from pydantic import BaseModel


class ProducerInterval(BaseModel):
    producer: str
    interval: int
    previousWin: int
    followingWin: int


class ProducerIntervalsResponse(BaseModel):
    min: List[ProducerInterval]
    max: List[ProducerInterval]
