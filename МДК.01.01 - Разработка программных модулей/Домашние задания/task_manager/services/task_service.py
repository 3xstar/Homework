import sys
sys.path.append('c:/VSCODE/pyqt/task_manager')
from db.conn import get_connection
import pandas as pd
from sqlalchemy import text

class TaskRepository:
    def get_all(self):
        engine = get_connection()
        query = "SELECT * FROM app.tasks ORDER BY id"
        df = pd.read_sql(query, engine)
        return df

    def add(self, title, description, status, priority):
        engine = get_connection()
        with engine.connect() as conn:
            conn.execute(text("""INSERT INTO app.tasks (title, description, status, priority)
                              VALUES (:title, :description, :status, :priority)"""),
                         {"title": title, "description": description, "status": status, "priority": priority})
            conn.commit()
        print(f"Задача {title} добавлена\n")
        self.reindex_ids()
        return self.get_all()

    def get_by_status(self, status):
        engine = get_connection()
        query = "SELECT * FROM app.tasks WHERE status = %s ORDER BY id"
        df = pd.read_sql(query, engine, params=(status,))
        print(f"Задачи найденные по статусу - {status}:")
        return df

    def update_status(self, task_id, new_status):
        engine = get_connection()
        with engine.connect() as conn:
            conn.execute(text("UPDATE app.tasks SET status = :new_status WHERE id = :task_id"),
                         {"new_status": new_status, "task_id": task_id})
            conn.commit()
        print(f"Статус задачи под id - {task_id} обновлен на: {new_status}\n")
        return self.get_all()

    def reset_sequence(self):
        engine = get_connection()
        with engine.connect() as conn:
            conn.execute(
                text("SELECT setval('app.tasks_id_seq', 1, false)")
            )
            conn.commit()
        print("Счётчик задач сброшен до 1")

    def reindex_ids(self):
        engine = get_connection()
        with engine.begin() as conn:
            result = conn.execute(text("SELECT id FROM app.tasks ORDER BY id"))
            rows = result.fetchall()
            
            if not rows:
                conn.execute(text("ALTER SEQUENCE app.tasks_id_seq RESTART WITH 1"))
                print("Таблица пуста, счётчик сброшен")
                return
            
            conn.execute(text("""
                CREATE TEMP TABLE tasks_temp AS 
                SELECT * FROM app.tasks ORDER BY id
            """))
            
            conn.execute(text("TRUNCATE TABLE app.tasks RESTART IDENTITY CASCADE"))
            
            conn.execute(text("""
                INSERT INTO app.tasks (title, description, status, priority)
                SELECT title, description, status, priority 
                FROM tasks_temp 
                ORDER BY id
            """))
            
            conn.execute(text("DROP TABLE tasks_temp"))
            
            conn.execute(text("""
                SELECT setval('app.tasks_id_seq', COALESCE((SELECT MAX(id) FROM app.tasks), 0))
            """))
            
        print("ID задач перенумерованы по порядку")

    def delete(self, task_id):
        engine = get_connection()
        with engine.connect() as conn:
            conn.execute(text("DELETE FROM app.tasks WHERE id = :task_id"),
                         {"task_id": task_id})
            conn.commit()
            print(f"Задача под id = {task_id} удалена\n")
        
        self.reindex_ids()
        
        return self.get_all()

    def reindex_ids_simple(self):
        engine = get_connection()
        with engine.begin() as conn:
            result = conn.execute(text("SELECT * FROM app.tasks ORDER BY id"))
            tasks = result.fetchall()
            
            if not tasks:
                conn.execute(text("ALTER SEQUENCE app.tasks_id_seq RESTART WITH 1"))
                return
            
            conn.execute(text("TRUNCATE TABLE app.tasks RESTART IDENTITY CASCADE"))
            
            for task in tasks:
                conn.execute(
                    text("""
                        INSERT INTO app.tasks (title, description, status, priority)
                        VALUES (:title, :description, :status, :priority)
                    """),
                    {
                        "title": task[1],
                        "description": task[2],
                        "status": task[3],
                        "priority": task[4]
                    }
                )
            
            print("ID задач перенумерованы по порядку")