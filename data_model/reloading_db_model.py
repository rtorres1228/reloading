from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, Numeric
from sqlalchemy.schema import ForeignKey, PrimaryKeyConstraint, Table
from sqlalchemy.orm import relationship

from database_engine import get_database_engine

Base = declarative_base()

DB_ENGINE = get_database_engine()

PARAMS = {
    'save-update': True,
    'delete': True,
    'delete-orphan': True,
    'merge': True
}


class Contributor(Base):
    """ contributor """

    __table_name = 'tbl_contributor'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    email = Column('email', String(255), primary_key=True, nullable=False)
    name = Column('name', String(255), nullable=True)
    calibers = relationship("Caliber", **PARAMS)


class Caliber(Base):
    """User account."""

    __tablename__ = "tbl_caliber"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    contributor_id = Column(Integer, ForeignKey('tbl_contributor.id'))
    caliber_name = Column('caliber_name', String(255), unique=True, nullable=False)
    load = relationship("Load", **PARAMS)


class Load(Base):
    """load"""

    __tablename__ = 'tbl_load'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    caliber_id = Column(Integer, ForeignKey='tbl_caliber.id')
    weight = Column('weight', Numeric, nullable=False)
    load_name = Column('load_name', String(255), unique=True, nullable=True)
    powder_charge = Column('powder_charge', Integer, nullable=False)
    # R or P
    primer_type = Column('primer_type', String(1), nullable=False)
    # L or S
    primer_size = Column('primer_size', String(1), nullable=False)
    primer_brand = Column('primer_brand', String(255), nullable=False)
    powder_brand = Column('powder_brand', String(255), nullable=False)
    # feet per second
    FPS = Column('FPS', Numeric, nullable=True)
    # power factor
    PF = Column('PF', Numeric, nullable=True)



