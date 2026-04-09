from dataclasses import dataclass
from typing import Optional
from enum import Enum

class TaskStatus(Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

@dataclass
class Task:
    id: Optional[int]
    title: str
    description: str
    status: TaskStatus
    priority: int
    
    def complete(self):
        """Бизнес-правило: завершение задачи"""
        self.status = TaskStatus.COMPLETED
    
    def is_valid(self) -> bool:
        """Бизнес-правило: валидация задачи"""
        return bool(self.title.strip()) and self.priority > 0