from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# --------------------- Define the User model ---------------------
class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
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

# --------------------- Define the Theme model ---------------------
class Theme(Base):
    __tablename__ = 'theme'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    # Define a relationship to the Event model
    events = relationship('Event', secondary='event_theme', back_populates='themes')

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

# -------------------- Define the Comment model --------------------
class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(500), nullable=False)
    date_created = Column(DateTime, nullable=False)

    # Foreign keys to User and Event models
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)

    # Define relationships to User and Event models
    user = relationship('User', back_populates='comments')
    event = relationship('Event', back_populates='comments')