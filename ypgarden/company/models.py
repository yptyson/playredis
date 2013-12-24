from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Sequence

engine =create_engine('mysql://root:123@localhost:3306/yy')
metadata = MetaData()

users_table = Table('users', metadata,
	Column('id', Integer, primary_key=True),
	Column('username', String(20), nullable = False),
	Column('fullname', String(20), nullable = False),
	Column('password', String(20), nullable = False),
	mysql_engine='InnoDB'
)

users2_table = Table('users2', metadata,
	Column('id', Integer, primary_key=True),
	Column('username', String(20), nullable = False),
	Column('fullname', String(20), nullable = False),
	mysql_engine='InnoDB'
)

metadata.create_all(engine)


class User(object):
    def __init__(self, username, fullname, password):
        self.username = username
        self.fullname = fullname
        self.password = password
mapper(User, users_table)

class User2(object):
    def __init__(self, username, fullname):
        self.username = username
        self.fullname = fullname

mapper(User2, users2_table)