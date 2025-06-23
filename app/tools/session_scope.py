from contextlib import contextmanager

@contextmanager
def SessionScope():
    """
    Context manager to handle session scope.
    
    This function ensures that the session is properly closed after use.
    
    :param session: The session object to manage.
    """
    from app import db # Import the db object from your app module

    # Create a new session from the db object
    session = db.session()

    # Ensure the session is closed after use
    try:  
        yield session       # Yield the session to be used in the context
        session.commit()    # Commit the session if no exceptions occur
    except Exception as e:  
        session.rollback()  # Rollback the session in case of an exception
        raise e             # Re-raise the exception for further handling
    finally:
        session.close()     # Close the session to release resources