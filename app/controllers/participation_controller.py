from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from flask_restful import Resource
from marshmallow import ValidationError

from app.models.db import Participation
from app.models.db.user_model import User
from app.models.dto.participation.participation_schema import ParticipationSchema
from app.tools.session_scope import SessionScope

class ParticipationController(Resource):
    # Demande de participation à un événement
    def request_participation(event_id):
        user_id = get_jwt_identity()  # ou méthode pour obtenir l'utilisateur connecté

        with SessionScope() as session:
            # Vérifie si participation existe déjà
            existing = session.query(Participation).filter_by(user_id=user_id, event_id=event_id).first()
            if existing:
                return jsonify({"message": "You have already requested participation"}), 400

            # Crée une nouvelle participation non confirmée
            participation = Participation(user_id=user_id, event_id=event_id, confirmed=False)
            session.add(participation)
            session.commit()

            return jsonify({"message": "Participation request submitted"}), 201
        
    # Get pending participations
    def get_pending_participations():
        with SessionScope() as session:
            participations = session.query(Participation).filter_by(confirmed=False).all()
            schema = ParticipationSchema(many=True)
            return jsonify(schema.dump(participations)), 200
        

    # confirm participation
    def confirm_participation(participation_id):
        # Récupère la participation par son ID
        with SessionScope() as session:
            # Vérifie si la participation existe
            participation = session.get(Participation, participation_id)
            # Si la participation n'existe pas, retourne une erreur
            if not participation:
                return jsonify({"message": "Participation not found"}), 404
            # Si la participation est déjà confirmée, retourne une erreur
            if participation.confirmed:
                return jsonify({"message": "Participation already confirmed"}), 400

            # Valide la participation
            participation.confirmed = True

            # Met à jour le rôle utilisateur si besoin
            user = session.get(User, participation.user_id)
            if user.role == "user":
                user.role = "participant"
                
            session.commit()

            return jsonify({"message": "Participation confirmed and user role updated"}), 200


