from app import app
from app.controllers.participation_controller import ParticipationController

from flask_jwt_extended import jwt_required
from app.tools.role_required import role_required

# Define the routes for participation-related operations

# Request participation for an event
@jwt_required()
@role_required("user")
@app.route('/participations/request/<int:event_id>', methods=['POST'])
def request_participation(event_id):
    return ParticipationController.request_participation(event_id)

# Get pending participations
@jwt_required()
@role_required("admin")
@app.route('/participations/pending', methods=['GET'])
def get_pending_participations():
    return ParticipationController.get_pending_participations()

# Confirm participation
@jwt_required()
@role_required("admin")
@app.route('/participations/confirm/<int:participation_id>', methods=['POST'])
def confirm_participation(participation_id):
    return ParticipationController.confirm_participation(participation_id)



