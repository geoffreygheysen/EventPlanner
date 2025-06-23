from sqlalchemy import Boolean, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import Base

# ----------------- Define the Participation model -----------------
class Participation(Base):
    __tablename__ = 'participation'

    id = Column(Integer, primary_key=True, index=True)
    confirmed = Column(Boolean, default=False, nullable=False)

    # Foreign keys to User and Event models
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)
    
    # Define relationships to User and Event models
    user = relationship('User', back_populates='participations')
    event = relationship('Event', back_populates='participations') 