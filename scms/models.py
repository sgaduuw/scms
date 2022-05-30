""" the models for the scms app """
import os

from ming import create_datastore, schema
from ming.odm import (FieldProperty, ForeignIdProperty, MappedClass, Mapper,
                      RelationProperty, ThreadLocalODMSession)

session = ThreadLocalODMSession(
    bind=create_datastore(os.getenv('MONGO_CONNECT'))
)

class Site(MappedClass):
    """ The model class for a site. """
    class __mongometa__:
        session = session
        name = 'site'

    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(schema.String)
    fqdns = FieldProperty(schema.Array(str))
    title = FieldProperty(schema.String)
    tagline = FieldProperty(schema.String)
    description = FieldProperty(schema.String)
    copyright = FieldProperty(schema.String)

    content = RelationProperty('Content')


class Content(MappedClass):
    """ The model class for a page. """
    class __mongometa__:
        session = session
        name = 'content'

    _id = FieldProperty(schema.ObjectId)
    title = FieldProperty(schema.String)
    text = FieldProperty(schema.String)
    date = FieldProperty(schema.DateTime)

    body = FieldProperty(schema.String)
    slug = FieldProperty(schema.String)
    publishdate = FieldProperty(schema.DateTime)
    description = FieldProperty(schema.String)

    # TODO
    # tags
    # categories
    # content_type

    site_id = ForeignIdProperty('Site')

Mapper.compile_all()
