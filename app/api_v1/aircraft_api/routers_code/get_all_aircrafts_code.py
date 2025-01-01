from sqlalchemy import select

from app.api_v1.error_messages import no_data
from app.core import async_session_maker, Aircraft


async def get_all_aircrafts_code():
    async with async_session_maker() as session:
        result = await session.execute(select(Aircraft))
        response = result.scalars().all()

        return response if response else no_data()
