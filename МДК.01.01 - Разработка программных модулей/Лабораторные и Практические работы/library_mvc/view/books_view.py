from view.base_view import BaseView
from typing import List, Dict

class BooksView(BaseView):
    def show_main_menu(self) -> str:
        self.clear_screen()
        self.show_header("📚 БИБЛИОТЕКА")
        print("1. 📖 Показать все книги")
        print("2. 🔍 Поиск книг")
        print("3. ➕ Добавить книгу")
        print("4. ✏️ Редактировать книгу")
        print("5. 🗑️ Удалить книгу")
        print("6. 🔄 Изменить доступность")
        print("7. 📊 Статистика")
        print("8. 🚪 Выход")
        print("=" * 60) # Увеличили ширину разделителя
        return input("\nВаш выбор: ").strip()

    def show_books(self, books: List[Dict], title: str = "Список книг"):
        self.show_header(title)
        if not books:
            print("\nСписок пуст")
            return
        
        # Добавили '{'Жанр':<15}' в заголовок таблицы
        print(f"\n{'ID':<4} {'Название':<25} {'Автор':<20} {'Год':<4} {'Жанр':<15} {'Статус':<10}")
        print("-" * 85) # Увеличили длину разделителя под новую ширину
        
        for book in books:
            status = "Доступна" if book['is_available'] else "Выдана"
            genre = book.get('genre', '') or "-" # Показываем прочерк, если жанр пуст
            
            # Обрезаем длинные строки для сохранения верстки
            t_disp = (book['title'][:23] + "...") if len(book['title']) > 25 else book['title']
            a_disp = (book['author'][:18] + "...") if len(book['author']) > 20 else book['author']
            g_disp = (genre[:13] + "...") if len(genre) > 15 else genre
            
            print(f"{book['id']:<4} {t_disp:<25} {a_disp:<20} {book['year']:<4} {g_disp:<15} {status:<10}")
        
        print(f"\nВсего книг: {len(books)}")

    def show_search_menu(self) -> tuple:
        self.show_header("Поиск книг")
        print("\nПоиск по:")
        print("1. Названию")
        print("2. Автору")
        print("3. Жанру") # Добавили поиск по жанру в меню
        print("4. Отмена")
        choice = input("\nВаш выбор: ").strip()
        
        if choice == '4':
            return None, None
            
        query = input("Введите запрос: ")
        
        # Логика выбора поля для поиска
        if choice == '1':
            field = 'title'
        elif choice == '2':
            field = 'author'
        elif choice == '3':
            field = 'genre'
        else:
            return None, None
            
        if field:
            return field, query
        return None, None

    def show_statistics(self, stats: Dict[str, int]):
        self.show_header("Статистика библиотеки")
        print(f"\nВсего книг:     {stats['total']}")
        print(f"Доступно:       {stats['total'] - stats['unavailable']}")
        print(f"Выдано:         {stats['unavailable']}")
        
        if stats['total'] > 0:
            percent = (stats['total'] - stats['unavailable']) / stats['total'] * 100
            print(f"📈 Доступность:    {percent:.1f}%")