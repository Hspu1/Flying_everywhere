from pydantic import BaseModel, Field


class SAircraft(BaseModel):
    name: str = Field(
        max_length=20,
        default="Название самолёта (до 20 символов)"
    )
    weight: int = Field(
        default="Вес самолёта в тоннах (целое число)", ge=1, le=999
    )
    length: int = Field(
        default="Длина самолёта в метрах (целое число)", ge=1, le=999
    )
