from sqlalchemy import Column, Integer, String, Date, DateTime
from datetime import datetime, UTC
from app.infra.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(String, default="pending")
    due_date = Column(Date)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))