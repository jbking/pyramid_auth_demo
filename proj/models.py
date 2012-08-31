from pyramid.security import Allow, Everyone
from sqlalchemy import (
    Column,
    Integer,
    Text,
    )
from sqlahelper import get_base

Base = get_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Integer)
 
    def __init__(self, name, value):
        self.name = name
        self.value = value

        """
        # acl can be an instance variable.
        self.__acl__ = [
            (Allow, Everyone, 'view'),
        ]
        """

    """
    # acl can be a class variable.
    __acl__ = [
        (Allow, Everyone, 'view'),
    ]
    """

    @property
    def __acl__(self):
        return [
            (Allow, Everyone, 'view'),
        ]
