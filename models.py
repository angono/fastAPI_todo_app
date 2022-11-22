from sqlalchemy import Column, Integer, String
from database import Base

class ItemModelTable(Base):
    __tablename__='items'
    id = Column(Integer, primary_key=True)
    task = Column(String(300))


