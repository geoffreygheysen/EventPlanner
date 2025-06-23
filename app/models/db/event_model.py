from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import Base

# --------------------- Define the Event model ---------------------
class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(200), nullable=False)
    status = Column(String(20), nullable=False)  # e.g., 'scheduled', 'completed', 'cancelled'
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)

    # Foreign key to the User model
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # Foreign key to the Theme model
    theme_id = Column(Integer, ForeignKey('theme.id'), nullable=False)
    
    # Define a relationship to the User model
    user = relationship('User', back_populates='events')
    # Define a relationship to the Theme model
    theme = relationship('Theme', back_populates='events')

    # Define a relationship to the Participation model
    participations = relationship('Participation', back_populates='event')
    # Define a relationship to the Comment model
    comments = relationship('Comment', back_populates='event')