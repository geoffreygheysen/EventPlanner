from app import app
from app.controllers.event_controller import EventController

from flask_jwt_extended import jwt_required
from app.tools.role_required import role_required

# Define the routes for event-related operations

# get all events
@app.route('/events', methods=['GET'])
def get_all_events():
    return EventController.get_all_events()

# get event by name
@app.route('/event/<string:name>', methods=['GET'])
def get_event_by_name(name):
    return EventController.get_event_by_name(name)

# get events by status
@app.route('/events/status/<string:status>', methods=['GET'])
def get_events_by_status(status):
    return EventController.get_events_by_status(status)

# get events by date
@app.route('/events/date/<string:date>', methods=['GET'])
def get_events_by_date(date):
    return EventController.get_events_by_date(date)

# create a new event
@jwt_required()
@role_required("admin")
@app.route('/event/create', methods=['POST'])
def create_event():
    return EventController.create_event()

# update event information
@jwt_required()
@role_required("admin")
@app.route('/event/update/<int:id>', methods=['PUT'])
def update_event(id):
    return EventController.update_event(id)

# delete event by id
@jwt_required()
@role_required("admin")
@app.route('/event/delete/<int:id>', methods=['DELETE'])
def delete_event(id):
    return EventController.delete_event_by_id(id)