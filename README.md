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

<details> 
<summary>SVG code</summary>

```
@endpoints.svg
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="endpoints.svg" version="1.1" width="121px" height="81px" viewBox="-0.5 -0.5 121 81" style="background-color: rgb(255, 255, 255);">
    <defs/>
    <g>
        <ellipse cx="60" cy="40" rx="60" ry="40" fill="#ffffff" stroke="#000000" pointer-events="all"/>
    </g>
</svg>
@endpoints.svg
```
</details>