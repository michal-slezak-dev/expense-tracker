from typing import List, Optional
from datetime import date, datetime, timezone
from sqlmodel import Field, Relationship, SQLModel

# User - id, username, email, password_hash, created_at, updated_at
# Category - id, name
# Expense - id, amount, description, date, created_at, updated_at

class User(SQLModel):
    id : Optional[int] = Field(default=None, primary_key=True) # SERIAL by default
    username : str = Field(unique=True, index=True, nullable=False)
    email : str = Field(unique=True, nullable=False)
    password_hash : str = Field(nullable=False)
    created_at : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at : datetime = Field(default=None)

    expenses : List['Expense'] = Relationship(back_populates='user')

class Category(SQLModel):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(unique=True, index=True, nullable=False)

    expenses : List['Expense'] = Relationship(back_populates='category')

class Expense(SQLModel):
    id : Optional[int] = Field(default=None, primary_key=True)
    amount : float = Field(default=0, decimal_places=2)
    description : Optional[str] = Field(default=None)
    date : date = Field(default_factory=date.today())
    created_at : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at : datetime = Field(default=None)

    category_id : Optional[int] = Field(default=None, foreign_key='category.id', ondelete='SET NULL')
    user_id : Optional[int] = Field(default=None, foreign_key='user.id', ondelete='CASCADE')

    category : Optional[Category] = Relationship(back_populates='expenses')
    user : Optional[User] = Relationship(back_populates='expenses')
