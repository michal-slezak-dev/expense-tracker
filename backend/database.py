from sqlmodel import SQLModel, create_engine, Session

postgres_url = 'postgresql+psycopg2://postgres:postgres@localhost:5432/expense_tracker'
engine = create_engine(postgres_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_Session():
    with Session(engine) as session:
        yield session
