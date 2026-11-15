from typing import Literal

from pydantic import BaseModel, Field


class MatchRequest(BaseModel):
    user_id: str = Field(min_length=1)
    role: Literal["host", "guest"]
    topic: str = Field(min_length=1)
    latitude: float
    longitude: float
    max_distance_meters: float


class MatchResponse(BaseModel):
    user_id: str
    role: str
