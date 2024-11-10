from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ESTA ES LA CADENA DE CONEXION SE DEBE DE CAMBIAR ESTA CADENA DE CONEXION...
URL_DATABASE = "postgresql://dpg-csn5skg8fa8c73ag3tv0-a.oregon-postgres.render.com:5432/project_db_0mzl?user=project_db_0mzl_user&password=POsrzlyY3Pqe54hfVNVOIImYlnXDQuuH"
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
