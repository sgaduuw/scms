from scms.extensions import db


class Site(db.Document):

    name = db.StringField(unique=True)
    fqdns = db.ListField(db.StringField())
    title = db.StringField()
    tagline = db.StringField()
    description = db.StringField()
    copyright = db.StringField()

    # content = RelationProperty('Content')
