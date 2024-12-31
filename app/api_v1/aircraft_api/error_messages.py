from fastapi import HTTPException


def cannot_create_aircraft():
    raise HTTPException(
        status_code=409,
        detail="Самолёт с таким названием уже существует"
    )
