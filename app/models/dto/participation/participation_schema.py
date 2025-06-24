from marshmallow import fields, Schema

class ParticipationSchema(Schema):
    confirmed = fields.Boolean(load_default=False)

    user_id = fields.Integer(required=True)
    event_id = fields.Integer(required=True)