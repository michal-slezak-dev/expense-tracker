from fastapi import APIRouter, Depends, HTTPException
from database import get_Session
from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import Session, select
from models import Category

router = APIRouter(prefix="/categories", tags=["categories"])

class CreateCategory(BaseModel):
    name : str

class CategoryResponse(BaseModel):
    id : int
    name : str

# add category
@router.post('/category', response_model=CategoryResponse)
async def create_category(category_request : CreateCategory, session : Session = Depends(get_Session)):
    try:
        category = Category(
        name=category_request.name,
        )

        session.add(category)
        session.commit()
        session.refresh(category)

        return category

    except Exception as e:
        session.delete(category)
        session.commit()
        raise HTTPException(status_code=500, detail=str(e))


# get categories
@router.get('/category', response_model=List[Category])
async def get_categories(session : Session = Depends(get_Session)):
    statement = select(Category)
    categories = session.exec(statement).all()

    return categories

# update category
# delete category