from app import app
from app.controllers.comment_controller import CommentController

from flask_jwt_extended import jwt_required
from app.tools.role_required import role_required

# Define the routes for comment-related operations

# get all comments for an event
@app.route('/event/<int:event_id>/comments', methods=['GET'])
def get_comments_by_event_id(event_id):
    return CommentController.get_comments_by_event_id(event_id)

# create a new comment for an event
@jwt_required()
@role_required("admin", "participant")
@app.route('/event/comments', methods=['POST'])
def create_comment():
    return CommentController.create_comment()

# delete a comment by id
@jwt_required()
@role_required("admin", "participant")
@app.route('/event/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    return CommentController.delete_comment(comment_id)