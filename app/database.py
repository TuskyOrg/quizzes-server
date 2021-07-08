from typing import Optional, Tuple, Any

from sqlalchemy.exc import OperationalError
from sqlalchemy.future import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import settings
from app.models import Base


def engine_and_Session(sqlalchemy_uri) -> Tuple[Any, sessionmaker]:
    engine = create_engine(settings.SQLALCHEMY_URI, echo=False)
    SessionLocal = sessionmaker(engine, autoflush=False, autocommit=False)
    return engine, SessionLocal


engine, SessionLocal = engine_and_Session(settings.SQLALCHEMY_URI)


def init_db() -> None:
    # We don't use Alembic yet
    Base.metadata.create_all(bind=engine)


def drop_db() -> None:
    # We don't use Alembic yet
    Base.metadata.drop_all(bind=engine)


def ping() -> Optional[Exception]:
    err = None
    try:
        s = SessionLocal()
        with s.connection():
            pass
    except OperationalError as _err:
        err = _err

    return err
