from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.engine import Engine
import os

data_dir = "data" if os.path.exists("data") else "."
postgres_file_name = "database.db"
postgres_url = f"postgresql+psycopg2:///{os.path.join(data_dir, postgres_file_name)}"

connect_args = {"check_same_thread": False} # allows multiuple threads to access the database!
engine = create_engine(postgres_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    with Session(engine) as session:
        yield session
