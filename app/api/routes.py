from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.infra.database import SessionLocal
from app.services.task_service import create_task, mark_done

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks")
def create(title: str, due_date: date, db: Session = Depends(get_db)):
    return create_task(db, title, due_date)

@router.put("/tasks/{task_id}/done")
def done(task_id: int, db: Session = Depends(get_db)):
    return mark_done(db, task_id)