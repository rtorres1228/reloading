from database_engine import Base, Session, engine
from data_model.reloading_db_model import Contributor, Caliber, Load
# boot strap
Base.metadata.create_all(engine)

session = Session()

contributor = Contributor('rtorres1228@yahoo.com', 'Roberto Torres')
caliber = Caliber('45 acp')
load = Load()

session.commit()
session.close()
