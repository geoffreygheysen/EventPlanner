from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from app.config import SECRET_KEY, URL_DB
from sqlalchemy.exc import SQLAlchemyError

from app.models.db import Base, User, Event, Theme, Participation, Comment

# Initialize Flask
app = Flask(__name__)

# Initialize SQLAlchemy
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database connection
db_connected = False

# Create the SQLAlchemy engine
try:

    # Create the Flask app and configure it
    db = SQLAlchemy(app)
    # Create the SQLAlchemy engine
    engine = create_engine(URL_DB)
    # Create the database metadata
    metadata = Base.metadata
    # Create all tables in the database
    db_connected = True

except SQLAlchemyError as e:

    # Handle any errors that occur during the connection
    print(f"Error connecting to the database: {e}")

if db_connected:

    # Delete all existing tables in the database
    # metadata.drop_all(bind=engine)
    # print("Existing database tables dropped successfully.")
    # Create all tables in the database
    metadata.create_all(bind=engine)

    from app.routes import user_routes

    print("-------------------------------------------")
    print(" ✅ Database tables created successfully ✅ ")
    print("-------------------------------------------")
