from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastapi_zero.settings import Settings

engine = create_engine(Settings().DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session