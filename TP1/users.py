from sqlalchemy import *
from sqlalchemy.sql import *

#Connecting to an Sqlite database located in memory (for tests)
#'echo' enables to log all the given SQL requests
engine = create_engine('sqlite:///:memory:', echo=True)

#Metadata object enables to save all the information about the manipulated database scheme
metadata = MetaData()

#Definition of a relationnal model with SQLAlchemy
users = Table('users', metadata, Column('id', Integer, autoincrement=True, primary_key=True), Column('name', String))

emails = Table('emails', metadata, Column('id', Integer, autoincrement=True, primary_key=True), Column('uid', None, ForeignKey('users.id')), Column('email', String, nullable=False))

#'create_all' creates WHEN NEEDED the corresponding tables to the specified scheme
metadata.create_all(engine)

#Connection is required
connection = engine.connect()

#We can work with our own databases
for row in connection.execute("select * from users"):
    print(row)
print('\n')

for row in connection.execute('select * from users where (name like ?) or (id > ?)', 'J%', 1):
    print(row)
print('\n')

#Close session (mandatory)
connection.close()
