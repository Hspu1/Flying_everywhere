from datetime import datetime

from pydantic import BaseModel, Field


class SFlight(BaseModel):
    flight_name: str = Field()
    departure_country: str = Field()
    departure_city: str = Field()
    departure_date_time: datetime = Field()
    arrival_country: str = Field()
    arrival_city: str = Field()
    arrival_date_time: datetime = Field()
    aircraft_name: str = Field()
    ticket_cost: int = Field()
