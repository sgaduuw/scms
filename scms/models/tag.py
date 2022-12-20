from scms.extensions import db


class Tag(db.Document):

    name = db.StringField(unique=True)
    slug = db.StringField()
    description = db.StringField()
