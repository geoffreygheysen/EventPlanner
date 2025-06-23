from marshmallow import Schema, ValidationError, fields, validate, validates_schema

class UserLoginSchema(Schema):
    email = fields.Email(required=True, validate=validate.Email())
    password = fields.String(required=True, validate=validate.Length(min=6))

class UserRegisterSchema(Schema):
    email = fields.Email(required=True, validate=validate.Email())
    password = fields.String(required=True, validate=validate.Length(min=6))
    confirm_password = fields.String(required=True, validate=validate.Length(min=6))

    @validates_schema
    def validate_password_match(self, data, **kwargs):
        if data.get('password') != data.get('confirm_password'):
            raise ValidationError("Passwords do not match", field_name="confirm_password")