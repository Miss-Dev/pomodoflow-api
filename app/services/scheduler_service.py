from apscheduler.schedulers.background import BackgroundScheduler
from app.services.task_service import get_pending_tasks_today
from app.services.notification_service import send_email
from app.infra.database import SessionLocal

scheduler = None


def check_tasks():
    db = SessionLocal()
    try:
        tasks = get_pending_tasks_today(db)

        for task in tasks:
            send_email(
                subject="Tarefa pendente",
                body=f"Tarefa pendente: {task.title}"
            )
    finally:
        db.close()


def start_scheduler():
    global scheduler

    if scheduler is None:
        scheduler = BackgroundScheduler()
        scheduler.add_job(check_tasks, "cron", hour=18, minute=0)
        scheduler.start()


def stop_scheduler():
    global scheduler

    if scheduler is not None:
        scheduler.shutdown()
        scheduler = None