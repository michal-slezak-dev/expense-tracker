from typing import List
from models import Expense

def calculate_expense_summary(expenses : List[Expense]):
    total = sum(e.amount for e in expenses)

    by_category = {}
    for e in expenses:
        by_category[e.category_id] = by_category.get(e.category_id, 0) + e.amount
    
    return {"total": total, "by_category": by_category}
