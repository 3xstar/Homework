from domain.models import Task, TaskStatus
from infrastructure.repositories import TaskRepository

class TaskService:
    def __init__(self):
        self.repository = TaskRepository()
    
    def create_task(self, title: str, description: str, 
                    status: str, priority: int) -> bool:
        """Бизнес-сценарий: создание задачи"""
        # Валидация (бизнес-логика, не UI!)
        if not title or not title.strip():
            raise ValueError("Название задачи не может быть пустым")
        if priority <= 0:
            raise ValueError("Приоритет должен быть больше 0")
        
        self.repository.add(title.strip(), description.strip(), 
                           status, priority)
        return True
    
    def change_status(self, task_id: int, new_status: str) -> bool:
        """Бизнес-сценарий: изменение статуса"""
        if task_id <= 0:
            raise ValueError("ID задачи должен быть положительным числом")
        
        valid_statuses = [s.value for s in TaskStatus]
        if new_status not in valid_statuses:
            raise ValueError(f"Недопустимый статус: {new_status}")
        
        self.repository.update_status(task_id, new_status)
        return True
    
    def remove_task(self, task_id: int) -> bool:
        """Бизнес-сценарий: удаление задачи"""
        if task_id <= 0:
            raise ValueError("ID задачи должен быть положительным числом")
        
        self.repository.delete(task_id)
        return True
    
    def get_all_tasks(self):
        """Бизнес-сценарий: получение всех задач"""
        return self.repository.get_all()
    
    def get_max_priority(self) -> int:
        return self.repository.get_max_priority()