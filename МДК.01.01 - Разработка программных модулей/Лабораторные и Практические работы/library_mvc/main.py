import sys
from pathlib import Path

# Добавляем корень проекта в path для импортов
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from data.db import Database
from model.book_model import BookModel
from view.books_view import BooksView
from view.book_form_view import BookFormView
from controller.book_controller import BookController
from controller.main_controller import MainController

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'library',
    'user': 'postgres',
    'password': '123'
}

def seed_data_if_empty(db: Database):
    """Простая функция инициализации, чтобы не засорять слои"""
    books = db.get_all_books()
    if not books:
        print("База пуста. Загружаем тестовые данные...")
        samples = [
            ("Война и мир", "Лев Толстой", 1869, "Роман", True),
            ("Преступление и наказание", "Федор Достоевский", 1866, "Роман", True),
            ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", False)
        ]
        for t, a, y, g, avail in samples:
            try:
                db.add_book(t, a, y, g, avail)
            except:
                pass # Игнорируем ошибки дубликатов если таблица уже есть данные
        print("Готово.")

def main():
    db = Database(DB_CONFIG)
    
    try:
        db.connect()
        print("✅ Подключение к БД успешно")
        
        # Инициализация данных (если нужно)
        seed_data_if_empty(db)

        # 1. Инициализация слоев
        model = BookModel(db)
        
        main_view = BooksView()
        form_view = BookFormView()
        
        # 2. Инициализация контроллеров
        book_ctrl = BookController(model, main_view, form_view)
        main_ctrl = MainController(book_ctrl, main_view)

        # 3. Запуск
        main_ctrl.run()

    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        print("Проверьте подключение к PostgreSQL и наличие БД 'library'")
    finally:
        db.close()

if __name__ == '__main__':
    main()