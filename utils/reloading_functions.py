import logging
from enum import Enum

LOGGER = logging.getLogger()

class Caliber(Enum):
    FORTYFIVE = '45acp'
    THIRTY8SPECIAL = '38spc'
    THREE08 = '308 win'

def get_load_caliber(caliber: Caliber):
    pass
