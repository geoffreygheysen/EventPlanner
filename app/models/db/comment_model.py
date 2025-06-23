from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import Base

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