from datetime import datetime
from scms.extensions import db
from scms.models import Site, Tag, Category


class Content(db.Document):

    title = db.StringField()
    body = db.StringField()
    create_date = db.DateTimeField(default=datetime.utcnow)
    publish_date = db.DateTimeField(default=datetime.utcnow)
    slug = db.StringField()
    description = db.StringField()
    site = db.ReferenceField(Site, required=True)
    tags = db.ListField(db.ReferenceField(Tag))
    categories = db.ListField(db.ReferenceField(Category))
