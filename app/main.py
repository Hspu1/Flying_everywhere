from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from uvicorn import run

from app.api_v1.aircraft_api import (
    create_aircraft, get_all_aircrafts, get_aircraft,
    update_aircraft_name, update_aircraft_data, delete_aircraft
)
from app.api_v1.flight_api import (
    create_flight, get_all_flights, get_flight, delete_flight
)

app = FastAPI(
    default_response_class=ORJSONResponse,
    title="Flying Everywhere"
)

app.include_router(create_aircraft)
app.include_router(get_all_aircrafts)
app.include_router(get_aircraft)
app.include_router(update_aircraft_name)
app.include_router(update_aircraft_data)
app.include_router(delete_aircraft)

app.include_router(create_flight)
app.include_router(get_all_flights)
app.include_router(get_flight)
app.include_router(delete_flight)


if __name__ == '__main__':
    run(app="main:app", port=8001, use_colors=True)
