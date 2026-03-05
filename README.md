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
│   ├── main.py          # Inicjalizacja apki i włączenie routerów
│   ├── database.py      # Konfiguracja silnika (Engine) i sesji
│   ├── models.py        # Definicje klas SQLModel (Table + Schemas)
│   └── routers/
│       ├── expenses.py  # Obsługa wydatków
│       └── categories.py# Obsługa kategorii
├── Dockerfile           # Budowanie obrazu Pythona
├── docker-compose.yml   # Orkiestracja API i bazy Postgres
└── requirements.txt     # sqlmodel, fastapi, uvicorn, psycopg2-binary

```

![alt text](endpoints.svg)