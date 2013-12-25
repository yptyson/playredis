from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from sqlalchemy import Sequence

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine =create_engine('mysql://root:123@localhost:3306/yy')
# metadata = MetaData()
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    fullname = Column(String(20))
    password = Column(String(20))
    addr=relationship("Addr",backref='users')
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

class Addr(Base):
    __tablename__ = 'addr'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(20), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
Base.metadata.create_all(engine)


# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child")
# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))

# Base.metadata.create_all(engine)




# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     child_id = Column(Integer, ForeignKey('child.id'))
#     child = relationship("Child")

# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)

# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     child = relationship("Child", uselist=False, backref="parent")

# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))

# Base.metadata.create_all(engine)


# association_table = Table('association', Base.metadata,
#     Column('left_id', Integer, ForeignKey('left.id')),
#     Column('right_id', Integer, ForeignKey('right.id'))
# )

# class Parent(Base):
#     __tablename__ = 'left'
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child",
#                     secondary=association_table)

# class Child(Base):
#     __tablename__ = 'right'
#     id = Column(Integer, primary_key=True)


# Base.metadata.create_all(engine)












