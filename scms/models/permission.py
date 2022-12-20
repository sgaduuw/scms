from scms.extensions import db


class Permission(db.Document):

    permission_name = db.StringField()
    description = db.StringField()
