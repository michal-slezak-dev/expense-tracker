from fastapi import APIRouter, Depends, HTTPException
from database import get_Session
from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import Session, select
from models import Category, User

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
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# get categories
@router.get('/category', response_model=List[Category])
async def get_categories(session : Session = Depends(get_Session)):
    statement = select(Category)
    categories = session.exec(statement).all()

    return categories

# update category
@router.put('/category/{category_id}', response_model=CategoryResponse)
async def update_category(category_id : int, new_name : str, session : Session = Depends(get_Session)):
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail='Category not found')

    category.name = new_name
    session.add(category)
    session.commit()

    return category
    

# delete category
@router.delete('/category/{category_id}')
async def delete_category(category_id : int, session : Session = Depends(get_Session)):
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail='Category not found')
    
    session.delete(category)
    session.commit()

    return {}


# seed endpoint... 1 user - hardcoded
@router.post('/seed')
async def seed(session : Session = Depends(get_Session)):
    user = User(
        username='test',
        email='test@gmail.com',
        password_hash='test_hash'
    )

    session.add(user)
    session.commit()

    return {'message': 'Test user added successfully'}
