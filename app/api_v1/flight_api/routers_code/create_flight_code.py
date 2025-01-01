from sqlalchemy.exc import IntegrityError

from app.api_v1.error_messages import no_object
from app.core import async_session_maker


async def create_flight_code(new_flight):
    try:
        async with async_session_maker() as session:
            async with session.begin():
                session.add(new_flight)

    except IntegrityError:
        return no_object()
