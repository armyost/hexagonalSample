import os

from sqlalchemy import (
    Column,
    MetaData,
    String, Integer, Float,
    Table,
    Text,
    ForeignKey,
    create_engine,
)

metadata = MetaData()

reports_table = Table(
    'report', metadata,
    Column('patient_id', String(250), primary_key=True),
    Column('document_text', Text, nullable=False)
)

users_table = Table(
    'user', metadata,
    Column('userId', Integer, primary_key=True),
    Column('description', Text, nullable=True),
    Column('userName', String(10), nullable=True),
    Column('deptId', Integer, ForeignKey("department.deptId"), nullable=True)
)

departments_table = Table(
    'department', metadata,
    Column('deptId', Integer, primary_key=True),
    Column('description', Text, nullable=True),
    Column('deptName', String(10), nullable=True)
)

def init_db_engine(db_uri=None):
    uri = db_uri or os.getenv('DB_URI')
    db_engine = create_engine(uri, convert_unicode=True, echo=True)
    __create_tables_if_not_exists(db_engine)
    return db_engine


def db_connect(db_engine):
    return db_engine.connect()


def close_db_connection(db_connection):
    try:
        db_connection.close()
    except:
        pass


def __create_tables_if_not_exists(db_engine):
    # NOTE:  use Alembic for migrations (https://alembic.sqlalchemy.org/en/latest/)
    reports_table.create(db_engine, checkfirst=True)
    users_table.create(db_engine, checkfirst=True)
    departments_table.create(db_engine, checkfirst=True)
