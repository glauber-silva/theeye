import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    created_dt = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)


class Session(BaseModel):
    __tablename__ = "sessions"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False,)


class Error(BaseModel):
    __tablename__ = "errors"

    data = db.Column(db.JSON, nullable=True)
    message = db.Column(db.String(200), nullable=True)


class Event(BaseModel):
    __tablename__ = "events"

    session = db.Column(db.ForeignKey("sessions.id", ondelete="CASCADE"))
    category = db.Column(db.String(50))
    name = db.Column(db.String(100))
    data = db.Column(db.JSON)
    timestamp = db.Column(db.DateTime)
