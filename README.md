# Expense Tracker

Nowoczesne API do zarządzania wydatkami domowymi. Projekt skupia się na wykorzystaniu **SQLModel**, który łączy zalety SQLAlchemy i Pydantica, zapewniając pełne wsparcie dla typowania danych i automatyczną dokumentację.

## Główne Cele Projektu

## Stos Technologiczny
* **Framework:** FastAPI
* **ORM & Validation:** [SQLModel](https://sqlmodel.tiangolo.com/) (SQLAlchemy + Pydantic)
* **Baza danych:** PostgreSQL
* **Serwer:** Uvicorn
* **Infrastruktura:** Docker & Docker Compose

## Struktura Projektu
```text
.
├── app/
│   ├── main.py          
│   ├── database.py      
│   ├── models.py        
│   └── routers/
│       ├── expenses.py  
│       └── categories.py
├── Dockerfile           
├── docker-compose.yml   
└── requirements.txt     

```

![alt text](endpoints.svg)
