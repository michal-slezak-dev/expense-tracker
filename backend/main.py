from fastapi import FastAPI
from routers import expenses, categories
from contextlib import asynccontextmanager
from database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Expense Tracker API"}

app.include_router(expenses.router)
app.include_router(categories.router)