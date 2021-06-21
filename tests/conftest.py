import pytest
import logging
from database_engine import Base, engine


@pytest.fixture
def boot_strap():
    Base.metadata.create_all(engine)


