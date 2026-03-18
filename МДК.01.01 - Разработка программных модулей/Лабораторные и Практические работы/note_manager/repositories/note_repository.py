from database.connection import get_connection

class NoteRepository:
    def get_all_notes(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT n.id, n.title, n.content, n.category_id, n.user_id, n.created_at, u.username
                FROM notes n
                JOIN users u ON n.user_id = u.id
                ORDER BY n.created_at DESC
            """)
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    def get_note_by_id(self, note_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notes WHERE id = %s", (note_id,))
            row = cursor.fetchone()
            return row
        finally:
            cursor.close()
            conn.close()

    def create_note(self, title, content, category_id, user_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO notes (title, content, category_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, content, category_id, user_id)
            )
            conn.commit()
            print(f"Записка: {title} добавлена")
        except Exception as e:
            print(f"Ошибка при создании: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def update_note(self, note_id, title, content, category_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE notes SET title = %s, content = %s, category_id = %s WHERE id = %s",
                (title, content, category_id, note_id)
            )
            conn.commit()
            print(f"Записка ID {note_id} успешно обновлена")
        except Exception as e:
            print(f"Ошибка при обновлении: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def remove_note(self, note_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
            conn.commit()
            print("Записка успешно удалена")
        except Exception as e:
            print(f"Ошибка при удалении: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def search_notes_by_title(self, search_text):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notes WHERE title ILIKE %s", (f"%{search_text}%",))
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    def get_notes_by_category(self, category_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notes WHERE category_id = %s", (category_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()