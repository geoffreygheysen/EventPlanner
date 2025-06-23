from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_model import Base

# --------------------- Define the Theme model ---------------------
class Theme(Base):
    __tablename__ = 'theme'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    # Define a relationship to the Event model
    events = relationship('Event', back_populates='theme')