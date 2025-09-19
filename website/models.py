from . import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import String, func, DateTime, ForeignKey
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship

# NOTE -> (flask_sqlalchemy) the way you create a model has changed in the newer version. the commented out code is what the tutorial uses.
class Note(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # data = db.Column(db.String(10000))
    # date = db.Column(db.DateTime(timezone=True), default=func.now())
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str] = mapped_column(String(length=10000))
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship("User", back_populates="notes")


class User(db.Model, UserMixin):
    # id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(150), unique= True)
    # password = db.Column(db.String(150))
    # first_name = db.Column(db.String(150))
    # notes = db.relationship("Note")
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(String(length=150))
    first_name: Mapped[str] = mapped_column(String(length=150))
    notes: Mapped[List["Note"]] = relationship("Note", back_populates="user")