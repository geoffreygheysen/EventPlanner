from flask_login import UserMixin
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from .base_model import Base

# --------------------- Define the User model ---------------------
class User(UserMixin, Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True) 
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    role = Column(String(20), nullable=False, default='user')  # e.g., 'admin', 'user', 'participant'
    active = Column(Boolean, default=True, nullable=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(512), nullable=False)

    # Define a relationship one-to-many to the Event model
    events = relationship('Event', back_populates='user')
    # Define a relationship one-to-many to the Participation model
    participations = relationship('Participation', back_populates='user')
    # Define a relationship one-to-many to the Comment model
    comments = relationship('Comment', back_populates='user')