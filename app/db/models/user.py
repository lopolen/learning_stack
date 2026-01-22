from datetime import datetime, date

from sqlalchemy import String, Integer, DateTime, Boolean, Date, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False)
    
    password_hash: Mapped[str] = mapped_column(
        String,
        nullable=False)
    
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    username: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )

    first_name: Mapped[str] = mapped_column(
        String,
        nullable=True
    )

    last_name: Mapped[str] = mapped_column(
        String,
        nullable=True
    )

    birthday: Mapped[date] = mapped_column(
        Date,
        nullable=True
    )

