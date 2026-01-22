from datetime import datetime

from sqlalchemy import String, DateTime, Boolean, Integer, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )
    
    password_hash: Mapped[str] = mapped_column(
        String,
        nullable=False)
    
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=text("true")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )
