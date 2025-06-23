from flask_login import UserMixin
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from .base_model import Base

# --------------------- Define the User model ---------------------
class User(UserMixin, Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True) 
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    role = Column(String(20), nullable=False)  # e.g., 'admin', 'user', 'participant'
    active = Column(Boolean, default=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    # Define a relationship one-to-many to the Event model
    events = relationship('Event', back_populates='user')
    # Define a relationship one-to-many to the Participation model
    participations = relationship('Participation', back_populates='user')
    # Define a relationship one-to-many to the Comment model
    comments = relationship('Comment', back_populates='user')