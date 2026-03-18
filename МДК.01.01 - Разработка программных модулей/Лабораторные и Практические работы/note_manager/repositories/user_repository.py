from database.connection import get_connection

class UserRepository:
    def get_all_users(self):
        """Получить всех пользователей"""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username FROM users ORDER BY id")
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    def get_user_by_id(self, user_id):
        """Получить пользователя по ID"""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username FROM users WHERE id = %s", (user_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    def get_user_by_username(self, username):
        """Получить пользователя по имени"""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username FROM users WHERE username = %s", (username,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    def create_user(self, username):
        """Создать нового пользователя"""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
            conn.commit()
            print(f"Пользователь: {username} добавлен")
        except Exception as e:
            print(f"Ошибка при создании пользователя: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def update_user(self, user_id, username):
        """Обновить имя пользователя"""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE users SET username = %s WHERE id = %s",
                (username, user_id)
            )
            conn.commit()
            print(f"Пользователь ID {user_id} успешно обновлен")
        except Exception as e:
            print(f"Ошибка при обновлении пользователя: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def remove_user(self, user_id):
        """Удалить пользователя"""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print(f"Пользователь ID {user_id} успешно удален")
        except Exception as e:
            print(f"Ошибка при удалении пользователя: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()