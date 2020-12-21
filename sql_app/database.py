from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#[baseDeDatos]://[usuario]:[pass]@[localhost]:[puerto]/[SID]
SQLALCHEMY_DATABASE_URL = 'oracle://ADMINPROCESS:Duoc2020@192.168.1.8:1521/XE'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#"max_identifier_length= 128"
