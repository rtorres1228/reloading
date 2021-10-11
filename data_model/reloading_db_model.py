from sqlalchemy import Column
from sqlalchemy.types import Integer, Text, String, Numeric
from sqlalchemy.schema import ForeignKey, PrimaryKeyConstraint, Table
from sqlalchemy.orm import relationship

from database_engine import Base


class Contributor(Base):
    """ contributor """

    __tablename__ = 'tbl_contributor'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    email = Column('email', String(255), unique=False, nullable=False)
    name = Column('name', String(255), nullable=True)
    calibers = relationship("Caliber")

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Caliber(Base):
    """User account."""
    __tablename__ = "tbl_caliber"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    contributor_id = Column(Integer, ForeignKey('tbl_contributor.id'))
    caliber_name = Column('caliber_name', String(255), unique=False, nullable=False)
    loads = relationship("Load")

    def __init__(self, caliber_name):
        self.caliber_name = caliber_name


class Load(Base):
    """load"""
    __tablename__ = 'tbl_load'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    caliber_id = Column(Integer, ForeignKey('tbl_caliber.id'))
    bullet_weight = Column('weight', Numeric, nullable=False)
    load_name = Column('load_name', String(255), unique=False, nullable=True)
    load_oal = Column('load_oal', String(255), unique=False, nullable=True)
    powder_charge = Column('powder_charge', Numeric, nullable=False)
    # R or P
    primer_type = Column('primer_type', String(1), nullable=False)
    # L or S
    primer_size = Column('primer_size', String(1), nullable=False)
    primer_brand = Column('primer_brand', String(255), nullable=False)
    powder_brand = Column('powder_brand', String(255), nullable=False)
    # feet per second
    fps = Column('fps', Numeric, nullable=True)
    # power factor
    pf = Column('pf', Numeric, nullable=True)

    oal = Column('oal', Numeric, nullable=True)

    def __init__(self, load_name, bullet_weight, powder_brand, powder_charge, primer_brand, primer_type, primer_size, fps=None,
                 pf=None, oal=None):
        self.load_name = load_name
        self.bullet_weight = bullet_weight
        self.powder_brand = powder_brand
        self.powder_charge = powder_charge
        self.primer_brand = primer_brand
        self.primer_type = primer_type
        self.primer_size = primer_size
        self.fps = fps
        self.pf = pf
        self.load_oal





