from datetime import datetime

from pydantic import BaseModel, Field


class SFlight(BaseModel):
    flight_name: str = Field(max_length=30)
    departure_country: str = Field(max_length=50)
    departure_city: str = Field(max_length=50)
    departure_date_time: datetime = Field()
    arrival_country: str = Field(max_length=50)
    arrival_city: str = Field(max_length=50)
    arrival_date_time: datetime = Field()
    aircraft_name: str = Field(max_length=20)
    ticket_cost_in_usd: int = Field()
