from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, Numeric
from database_engine import get_database_engine

Base = declarative_base()

DB_ENGINE = get_database_engine()

class Caliber(Base):
    """User account."""

    __tablename__ = "tbl_caliber"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    caliber_name = Column('caliber_name', String(255), unique=True, nullable=False)

class Weight(Base):
    """bullet weight"""

    __tablename__ = 'tbl_weight'

    id = Column(Integer, primary_key=True, autoincrement="auto")
    # bullet weight
    weight = Column('weight', Numeric, nullable=False)

class Load(Base):
    """load"""

    __tablename__ = 'tbl_load'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    load_name = caliber_name = Column('load_name', String(255), unique=True, nullable=False)
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

class Contributor(Base):
    """ contributor """
    __table_name = 'tbl_contributor'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    email = Column('email', String(255), nullable=False)
    name = Column('name', String(255), nullable=True)
