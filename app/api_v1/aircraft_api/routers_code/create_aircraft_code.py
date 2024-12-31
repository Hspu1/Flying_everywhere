from sqlalchemy.exc import IntegrityError

from app.api_v1.aircraft_api.error_messages import cannot_create_aircraft
from app.core import async_session_maker


async def create_aircraft_code(new_aircraft):
    try:
        async with async_session_maker() as session:
            async with session.begin():
                session.add(new_aircraft)

    except IntegrityError:
        return cannot_create_aircraft()
