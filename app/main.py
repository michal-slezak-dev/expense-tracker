from fastapi import FastAPI
from .routers import expenses, categories

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Expense Tracker API"}

app.include_router(expenses.router)
app.include_router(categories.router)