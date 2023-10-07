from .base import Base, Session, engine
from .model import Data

__all__ = [
    "Data",
    "Base",
    "Session",
    "engine"
]

def migrate():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    