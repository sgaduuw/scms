from scms.extensions import db
from scms.models import Permission


class Group(db.Document):

    group_name = db.StringField()
    permissions = db.ListField(db.ReferenceField(Permission))
