from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String
from database_engine import get_database_engine

Base = declarative_base()

DB_ENGINE = get_database_engine()

class Caliber(Base):
    """User account."""

    __tablename__ = "tbl_caliber"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    caliber_name = Column(String(255), unique=True, nullable=False)

class Weight(Base):
    """bullet weight"""

    __tablename__ = 'tbl_weight'

    id = Column(Integer, primary_key=True, autoincrement="auto")
    # bullet weight
    weight = Column(Integer, nullable=False)

class Load(Base):
    """load"""

    __tablename__ = 'tbl_load'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    load_name = caliber_name = Column(String(255), unique=True, nullable=False)
    powder_charge = Column(Integer, nullable=False)
    # R or P
    primer_type = Column(String(1), nullable=False)
    # L or S
    primer_size = Column(String(1), nullable=False)
    primer_brand = Column(String(255), nullable=False)
    powder_brand = Column(String(255), nullable=False)
    # feet per second
    FPS = Column(Integer, nullable=True)
    # power factor
    PF = Column(Integer, nullable=True)

class Contributor(Base):
    """ contributor """
    __table_name = 'tbl_contributor'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    email = Column(String(255), nullable=False)
    name = Column(String(255), nullable=True)
