import datetime
from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models.db.comment_model import Comment
from app.models.dto.comment.comment_schema import CommentSchema
from app.models.db.event_model import Event
from app.tools.session_scope import SessionScope

class CommentController(Resource):
    # Get all comments for an event
    def get_comments_by_event_id(event_id):
        with SessionScope() as session:
            event = session.get(Event, event_id)
            if not event:
                return jsonify({"message": "Event not found"}), 404

            comments = event.comments  # accède directement à la relation avec event
            if not comments:
                return jsonify({"message": "No comments found for this event"}), 404

            comment_schema = CommentSchema(many=True)
            comment_serialized = comment_schema.dump(comments)
            return jsonify(comment_serialized), 200

    
    # Create a new comment for an event
    def create_comment():
        comment_schema = CommentSchema()
        try:
            comment_data = comment_schema.load(request.json)
        except ValidationError as e:
            return jsonify({"message": str(e)}), 400

        with SessionScope() as session:
            # Vérifie que l'événement existe
            event = session.get(Event, request.json["event_id"])
            if not event:
                return jsonify({"message": "Event not found"}), 404
            
            # Vérifie que l'événement est passé
            if event.date_end > datetime.datetime.now():
                return jsonify({"message": "Cannot comment on a future event"}), 400

            # Crée le commentaire en liant l'event_id
            new_comment = Comment(**comment_data)

            session.add(new_comment)
            session.commit()

            return jsonify({"message": "Comment created successfully"}), 201
        
    # Delete a comment by its ID
    def delete_comment(comment_id):
        with SessionScope() as session:
            comment = session.get(Comment, comment_id)
            if not comment:
                return jsonify({"message": "Comment not found"}), 404
            
            session.delete(comment)
            session.commit()

            return jsonify({"message": "Comment deleted successfully"}), 200


    
    
