from sqlalchemy import select

from app.api_v1.error_messages import no_data
from app.core import async_session_maker, Flight


async def get_all_flights_code():
    async with async_session_maker() as session:
        result = await session.execute(select(Flight))
        response = result.scalars().all()

        return response if response else no_data(correction="полёта")
