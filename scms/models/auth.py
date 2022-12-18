from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from scms.extensions import db


class Permission(db.Document):

    permission_name = db.StringField()
    description = db.StringField()


class Group(db.Document):

    group_name = db.StringField()
    permissions = db.ListField(db.ReferenceField(Permission))


class User(UserMixin, db.Document):

    first_name = db.StringField()
    last_name = db.StringField(unique_with='first_name')
    user_name = db.StringField(required=True, unique=True)
    email = db.StringField()

    groups = db.ListField(db.ReferenceField(Group))

    password_hash = db.StringField()
    created = db.DateTimeField(default=datetime.utcnow)

    def get_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
