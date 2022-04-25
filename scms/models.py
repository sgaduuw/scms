from ming import create_datastore
from ming.odm import ThreadLocalODMSession

from ming import schema
from ming.odm import MappedClass
from ming.odm import FieldProperty, ForeignIdProperty

from ming.odm import Mapper


session = ThreadLocalODMSession(
    bind=create_datastore('mim:///tutorial')
)
session

class Site(MappedClass):
    class __mongometa__:
        session = session
        name = 'site'
    
    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(schema.String(required=True))

class WikiPage(MappedClass):
    class __mongometa__:
        session = session
        name = 'wiki_page'

    _id = FieldProperty(schema.ObjectId)
    title = FieldProperty(schema.String(required=True))
    text = FieldProperty(schema.String(if_missing=''))

Mapper.compile_all()

print(session.db)
print(session.bind)
