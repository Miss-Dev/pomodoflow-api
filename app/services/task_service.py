from sqlalchemy.orm import Session
from app.domain.models import Task
from datetime import date

def create_task(db: Session, title: str, due_date: date):
    task = Task(title=title, due_date=due_date)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_pending_tasks_today(db: Session):
    today = date.today()
    return db.query(Task).filter(
        Task.status == "pending",
        Task.due_date <= today
    ).all()

def mark_done(db: Session, task_id: int):
    task = db.query(Task).get(task_id)
    task.status = "done"
    db.commit()
    return task