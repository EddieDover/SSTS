from contextlib import contextmanager

from sqlalchemy import Engine
from sqlmodel import Session

@contextmanager
def get_session(engine: Engine) -> Session:
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()