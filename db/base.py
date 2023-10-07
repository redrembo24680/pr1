from sqlalchemy.orm import declarative_base
from settings import Settings
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

logging.basicConfig(level=logging.INFO)

engine = create_engine(Settings.DATABASE)
# meta = Base.metadata
# session = Session(engine)
Session = sessionmaker(bind=engine)
