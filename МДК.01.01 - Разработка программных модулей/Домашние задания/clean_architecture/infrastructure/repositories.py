import pandas as pd
from sqlalchemy import text
from domain.models import Task, TaskStatus
from infrastructure.database import get_connection

class TaskRepository:
    def get_all(self) -> pd.DataFrame:
        engine = get_connection()
        query = "SELECT * FROM app.tasks ORDER BY id"
        return pd.read_sql(query, engine)
    
    def add(self, title: str, description: str, status: str, priority: int):
        engine = get_connection()
        with engine.connect() as conn:
            conn.execute(text("""
                INSERT INTO app.tasks (title, description, status, priority)
                VALUES (:title, :description, :status, :priority)
            """), {"title": title, "description": description, 
                   "status": status, "priority": priority})
            conn.commit()
        self.reindex_ids()
    
    def update_status(self, task_id: int, new_status: str):
        engine = get_connection()
        with engine.connect() as conn:
            conn.execute(text(
                "UPDATE app.tasks SET status = :new_status WHERE id = :task_id"
            ), {"new_status": new_status, "task_id": task_id})
            conn.commit()
        return self.get_all()
    
    def delete(self, task_id: int):
        engine = get_connection()
        with engine.connect() as conn:
            conn.execute(text(
                "DELETE FROM app.tasks WHERE id = :task_id"
            ), {"task_id": task_id})
            conn.commit()
        self.reindex_ids()
    
    def reindex_ids(self):
        engine = get_connection()
        with engine.begin() as conn:
            result = conn.execute(text("SELECT id FROM app.tasks ORDER BY id"))
            rows = result.fetchall()
            if not rows:
                conn.execute(text("ALTER SEQUENCE app.tasks_id_seq RESTART WITH 1"))
                return
            conn.execute(text("""
                CREATE TEMP TABLE tasks_temp AS 
                SELECT * FROM app.tasks ORDER BY id
            """))
            conn.execute(text("TRUNCATE TABLE app.tasks RESTART IDENTITY CASCADE"))
            conn.execute(text("""
                INSERT INTO app.tasks (title, description, status, priority)
                SELECT title, description, status, priority 
                FROM tasks_temp ORDER BY id
            """))
            conn.execute(text("DROP TABLE tasks_temp"))
            conn.execute(text("""
                SELECT setval('app.tasks_id_seq', 
                    COALESCE((SELECT MAX(id) FROM app.tasks), 0))
            """))
    
    def get_max_priority(self) -> int:
        df = self.get_all()
        if df.empty:
            return 0
        return int(df['priority'].max())