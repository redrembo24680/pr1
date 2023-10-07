from sqlalchemy import Column, Unicode, BigInteger

from .. import Base

__all__ = ['Base']

class Data(Base):
    __tablename__ = 'data'

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    first_name =Column(
    Unicode,
    nullable=False
    )
    second_name =Column( 
    Unicode,
    nullable=False
    )
    tel_number = Column(
        Unicode,
        nullable=False
    )
