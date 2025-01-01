from pydantic import BaseModel, Field

from app.core import async_session_maker


class SAircraft(BaseModel):
    name: str = Field(
        max_length=20,
        default="Название самолёта (до 20 символов)"
    )
    weight_in_tons: int = Field(
        default="Вес самолёта в тоннах (целое число)", ge=1, le=999
    )
    length_in_meters: int = Field(
        default="Длина самолёта в метрах (целое число)", ge=1, le=999
    )


async def aircraft_existence(query) -> bool:
    async with async_session_maker() as session:
        res = await session.execute(query)

        return res.scalars().first() is not None
