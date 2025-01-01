from pydantic import BaseModel


class SFlight(BaseModel):
    flight_name
    departure_country
    departure_city
    departure_date_time
    arrival_country
    arrival_city
    arrival_date_time
    aircraft_name
    ticket_cost
