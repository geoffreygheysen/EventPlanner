from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models.db import Event
from app.models.dto.event.event_schema import EventSchema
from app.models.dto.event.event_update_schema import EventUpdateSchema
from app.tools.session_scope import SessionScope

class EventController(Resource):
    # get all events
    def get_all_events():
        with SessionScope() as session:
            events = session.query(Event).all()
            event_schema = EventSchema(many=True)
            event_serialized = event_schema.dump(events)
        return jsonify(event_serialized), 200
    
    # get event by name
    def get_event_by_name(name):
        with SessionScope() as session:
            event = session.query(Event).filter_by(name=name).first()
            if not event:
                return jsonify({"message": "Event not found"}), 404
            
            event_schema = EventSchema()
            event_serialized = event_schema.dump(event)
        return jsonify(event_serialized), 200
    
    # Get events by status
    def get_events_by_status(status):
        with SessionScope() as session:
            events = session.query(Event).filter_by(status=status).all()
            if not events:
                return jsonify({"message": "No events found with the specified status"}), 404
            
            event_schema = EventSchema(many=True)
            event_serialized = event_schema.dump(events)
        return jsonify(event_serialized), 200
    
    # Get events by date
    def get_events_by_date(date):
        with SessionScope() as session:
            events = session.query(Event).filter(Event.date_start <= date, Event.date_end >= date).all()
            if not events:
                return jsonify({"message": "No events found for the specified date"}), 404
            
            event_schema = EventSchema(many=True)
            event_serialized = event_schema.dump(events)
        return jsonify(event_serialized), 200
    
    # Create a new event
    def create_event():
        event_schema = EventSchema()
        try:
            event_data = event_schema.load(request.json)
        except ValidationError as e:
            return jsonify({"message": str(e)}), 400
        
        with SessionScope() as session:
            new_event = Event(**event_data)
            session.add(new_event)
            session.commit()
            event_serialized = event_schema.dump(new_event)
        return jsonify(event_serialized), 201
    
    # Update event information
    def update_event(id, event_data):
        event_schema = EventUpdateSchema()
        try:
            event_data = event_schema.load(request.json, partial=True)
        except ValidationError as e:
            return jsonify({"message": str(e)}), 400
        
        with SessionScope() as session:
            event = session.query(Event).get(id)
            if not event:
                return jsonify({"message": "Event not found"}), 404
            
            for key, value in event_data.items():
                setattr(event, key, value)
            
            session.commit()
            event_serialized = event_schema.dump(event)
        return jsonify(event_serialized), 200
    
    # Delete event by id
    def delete_event_by_id(id):
        with SessionScope() as session:
            event = session.query(Event).get(id)
            if event:
                session.delete(event)
                session.commit()
                return jsonify({"message": "Event deleted successfully"}), 200
            else:
                return jsonify({"message": "Event not found"}), 404