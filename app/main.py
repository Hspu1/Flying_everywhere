from fastapi import FastAPI
from uvicorn import run

from app.api_v1.aircraft_api import (
    create_aircraft, get_all_aircrafts, get_aircraft
)


app = FastAPI(
    title="Flying Everywhere"
)

app.include_router(create_aircraft)
app.include_router(get_all_aircrafts)
app.include_router(get_aircraft)


if __name__ == '__main__':
    run(app="main:app", use_colors=True)
