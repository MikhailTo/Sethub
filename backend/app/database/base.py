from typing import Any
from sqlalchemy.orm import declarative_base

class DatabaseBase():
    def generate_base(self) -> Any:
        """
        Generate a declarative base for ORM models.
        """
        base = declarative_base()
        return base

Base: Any = DatabaseBase().generate_base()
