from marshmallow import Schema, fields, validates_schema, post_load, validate, ValidationError


class ErrorSchema(Schema):
    id = fields.Integer()
    created_at = fields.DateTime()
    data = fields.Dict(required=True)
    message = fields.String(required=True)
