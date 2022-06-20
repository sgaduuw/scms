""" the models for the scms app """
import os
from datetime import datetime
from hashlib import sha256

from ming import create_datastore, schema
from ming.odm import (FieldProperty, ForeignIdProperty, MappedClass, Mapper,
                      RelationProperty, ThreadLocalODMSession)

m_session = ThreadLocalODMSession(
    bind=create_datastore(os.getenv('MONGO_CONNECT'))
)

class Site(MappedClass):
    """ The model class for a site. """
    class __mongometa__:
        session = m_session
        name = 'site'
        unique_indexes = [('name',),]

    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(schema.String, unique=True)
    fqdns = FieldProperty(schema.Array(str))
    title = FieldProperty(schema.String)
    tagline = FieldProperty(schema.String)
    description = FieldProperty(schema.String)
    copyright = FieldProperty(schema.String)

    content = RelationProperty('Content')


class Content(MappedClass):
    """ The model class for a page. """
    class __mongometa__:
        session = m_session
        name = 'content'

    _id = FieldProperty(schema.ObjectId)
    title = FieldProperty(schema.String)
    body = FieldProperty(schema.String)
    create_date = FieldProperty(schema.DateTime)
    publish_date = FieldProperty(schema.DateTime)
    slug = FieldProperty(schema.String)
    description = FieldProperty(schema.String)

    # TODO
    # tags
    # categories
    # content_type

    site_id = ForeignIdProperty('Site')


class Group(MappedClass):
    """
    Group definition.
    """
    class __mongometa__:
        session = m_session
        name = 'auth_group'
        unique_indexes = [('group_name',),]

    _id = FieldProperty(schema.ObjectId)
    group_name = FieldProperty(schema.String)

    permissions = RelationProperty('Permission')


class Permission(MappedClass):
    """
    Permission definition.
    """
    class __mongometa__:
        session = m_session
        name = 'auth_permission'
        unique_indexes = [('permission_name',),]

    _id = FieldProperty(schema.ObjectId)
    permission_name = FieldProperty(schema.String)
    description = FieldProperty(schema.String)

    _groups = ForeignIdProperty(Group, uselist=True)
    groups = RelationProperty(Group)


class User(MappedClass):
    """
    User definition.
    This is the user definition used by :mod:`repoze.who`, which requires at
    least the ``user_name`` column.
    """
    class __mongometa__:
        session = m_session
        name = 'auth_user'
        unique_indexes = [('user_name',),]

    class PasswordProperty(FieldProperty):
        @classmethod
        def _hash_password(cls, password):
            salt = sha256()
            salt.update(os.urandom(60))
            salt = salt.hexdigest()

            l_hash = sha256()
            # Make sure password is a str because we cannot hash unicode objects
            l_hash.update((password + salt).encode('utf-8'))
            l_hash = l_hash.hexdigest()

            password = salt + l_hash
            print(password)

            return password

        def __set__(self, instance, value):
            value = self._hash_password(value)
            return FieldProperty.__set__(self, instance, value)

    _id = FieldProperty(schema.ObjectId)
    first_name = FieldProperty(schema.String)
    last_name = FieldProperty(schema.String)
    username = FieldProperty(schema.String)

    _groups = ForeignIdProperty(Group, uselist=True)
    groups = RelationProperty(Group)

    password = PasswordProperty(schema.String)
    created = FieldProperty(schema.DateTime, if_missing=datetime.now)

    @property
    def permissions(self):
        return Permission.query.find(dict(_groups={'$in':self._groups})).all()

    @classmethod
    def by_email_address(cls, email):
        """Return the user object whose email address is ``email``."""
        return cls.query.get(email_address=email)

    def validate_password(self, password):
        """
        Check the password against existing credentials.
        :param password: the password that was provided by the user to
            try and authenticate. This is the clear text version that we will
            need to match against the hashed one in the database.
        :type password: unicode object.
        :return: Whether the password is valid.
        :rtype: bool
        """
        l_hash = sha256()
        l_hash.update((password + self.password[:64]).encode('utf-8'))
        return self.password[64:] == l_hash.hexdigest()


Mapper.compile_all()
