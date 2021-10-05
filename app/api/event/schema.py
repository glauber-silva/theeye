import logging
from datetime  import datetime

from marshmallow import Schema, fields, validates_schema, post_load, validate, ValidationError

from app.databases.models import Event

logger = logging.getLogger(__name__)


class EventSchema(Schema):

    @validates_schema
    def validate_timestamp(self, data, **kwargs):
        timestamp = data.get("timestamp")
        if timestamp:
            if timestamp > datetime.now():
                raise ValidationError("future timestamp")

    session_id = fields.UUID(required=True)
    category = fields.String(required=True)
    name = fields.String(required=True)
    data = fields.Dict(required=True)
    timestamp = fields.DateTime(required=True)

    @post_load
    def make_event(self, data, **kwargs):
        return Event(**data)
