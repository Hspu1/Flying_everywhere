from fastapi import FastAPI
from uvicorn import run

from app.api_v1.aircraft_api import create_aircraft


app = FastAPI(
    title="Flying Everywhere"
)

app.include_router(create_aircraft)


if __name__ == '__main__':
    run(app="main:app", use_colors=True)
