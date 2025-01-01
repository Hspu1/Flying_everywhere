__all__ = (
    "create_aircraft",
    "get_all_aircrafts",
    "get_aircraft",
    "update_aircraft_name",
    "delete_aircraft"
)

from .aircraft_routers import (
    create_aircraft, get_all_aircrafts, get_aircraft,
    update_aircraft_name, delete_aircraft
)
