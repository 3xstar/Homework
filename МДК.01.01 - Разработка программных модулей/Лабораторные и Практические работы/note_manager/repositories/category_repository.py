from database.connection import get_connection

class CategoryRepository:
    def get_all_categories(self):
        """Получить все категории"""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM categories ORDER BY id")
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    def get_category_by_id(self, category_id):
        """Получить категорию по ID"""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM categories WHERE id = %s", (category_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    def create_category(self, name):
        """Создать новую категорию"""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO categories (name) VALUES (%s)", (name,))
            conn.commit()
            print(f"Категория: {name} добавлена")
        except Exception as e:
            print(f"Ошибка при создании категории: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def update_category(self, category_id, name):
        """Обновить название категории"""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE categories SET name = %s WHERE id = %s",
                (name, category_id)
            )
            conn.commit()
            print(f"Категория ID {category_id} успешно обновлена")
        except Exception as e:
            print(f"Ошибка при обновлении категории: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def remove_category(self, category_id):
        """Удалить категорию"""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM categories WHERE id = %s", (category_id,))
            conn.commit()
            print(f"Категория ID {category_id} успешно удалена")
        except Exception as e:
            print(f"Ошибка при удалении категории: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()