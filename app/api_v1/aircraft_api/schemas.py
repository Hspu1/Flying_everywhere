from pydantic import BaseModel, Field


class SAircraft(BaseModel):
    name: str = Field(
        max_length=20,
        default="Название самолёта (до 20 символов)"
    )
    weight: int = Field(
        max_digits=3,
        default="Вес самолёта в тоннах (целое значение)"
    )
    length: int = Field(
        max_digits=2,
        default="Длина самолёта в метрах (целое значение)"
    )
