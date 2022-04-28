import os
import datetime
from ming import Session, create_datastore
from ming import Document, Field, schema
#from ming.odm import MappedClass
#from ming.odm import FieldProperty, ForeignIdProperty
#from ming.odm import ThreadLocalODMSession
from ming.odm import Mapper

session = Session(create_datastore(os.getenv('MONGO_CONNECT')))
class Site(Document):
    class __mongometa__:
        session = session
        name = 'site'

    m: 'Manager[Site]'
    
    _id = Field(schema.ObjectId)
    name = Field(str)

class Page(Document):
    class __mongometa__:
        session = session
        name = 'page'

    m: 'Manager[Page]'

    _id = Field(schema.ObjectId)
    title = Field(str)
    text = Field(str)

Mapper.compile_all()

print(session.db)
print(session.bind)
