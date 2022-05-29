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

    page = RelationProperty('Page')


class Page(MappedClass):
    """ The model class for a page. """
    class __mongometa__:
        session = session
        name = 'page'

    _id = FieldProperty(schema.ObjectId)
    title = FieldProperty(schema.String)
    text = FieldProperty(schema.String)
    date = FieldProperty(schema.DateTime)
    site_id = ForeignIdProperty('Site')

Mapper.compile_all()
