from sqlalchemy.exc import IntegrityError

from app.api_v1.error_messages import cannot_create_new_object
from app.core import async_session_maker


async def create_aircraft_code(new_aircraft):
    try:
        async with async_session_maker() as session:
            async with session.begin():
                session.add(new_aircraft)

    except IntegrityError:
        return cannot_create_new_object(correction="Самолёт")
