from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import Session, Field, select
from datetime import date
from database import get_Session
from services.expense_service import calculate_expense_summary 
from models import Expense, Category, User
from datetime import datetime, timezone, timedelta

router = APIRouter(prefix="/expenses", tags=["expenses"])

class CreateExpense(BaseModel):
    name : str
    amount : float
    description : Optional[str]
    expense_date : Optional[date]
    category_id : int

class UpdateExpense(CreateExpense):
    pass


# add expense
@router.post('/expense')
async def create_expense(expense_request : CreateExpense, session : Session = Depends(get_Session)):
    try:
        expense = Expense(
            name=expense_request.name,
            amount=expense_request.amount,
            description=expense_request.description,
            expense_date=expense_request.expense_date,
            user_id=1,
            category_id=1
        )

        session.add(expense)
        session.commit()
        session.refresh(expense)

        return expense
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# get expenses
@router.get('/expense', response_model=List[Expense])
async def get_expenses(session : Session = Depends(get_Session)):
    statement = select(Expense)
    expenses = session.exec(statement).all()

    return expenses

# update expense
@router.put('/expense/{expense_id}', response_model=Expense)
async def update_expense(expense_id : int, expense_request : UpdateExpense, session : Session = Depends(get_Session)):
    expense = session.get(Expense, expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail='Expense not found')
    
    expense_data = expense_request.model_dump(exclude_unset=True) # incluce only fields that have been changed
    for key, value in expense_data.items():
        setattr(expense, key, value)
    
    expense.updated_at = datetime.now(timezone.utc)
    
    session.add(expense)
    session.commit()

    return expense

# delete expense
@router.delete('/expense/{expense_id}')
async def delete_expense(expense_id : int, session : Session = Depends(get_Session)):
    expense = session.get(Expense, expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    session.delete(expense)
    session.commit()

    return {}

# get expense summary
@router.get('/summary')
def get_expense_summary(session : Session = Depends(get_Session)):
    """
    Get monthly expense summary (base) regardless of user_id (for now)
    """
    interval = datetime.now(timezone.utc) - timedelta(days=30)
    statement = select(Expense).where(Expense.expense_date >= interval)
    
    expenses = session.exec(statement).all()

    return calculate_expense_summary(expenses)
    