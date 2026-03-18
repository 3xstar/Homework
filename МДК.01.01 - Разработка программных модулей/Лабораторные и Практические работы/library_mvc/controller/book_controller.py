from model.book_model import BookModel, BookValidationError, BookNotFoundError
from view.books_view import BooksView
from view.book_form_view import BookFormView

class BookController:
    def __init__(self, model: BookModel, view: BooksView, form_view: BookFormView):
        self.model = model
        self.view = view
        self.form_view = form_view

    def show_all(self):
        books = self.model.get_all_books()
        self.view.show_books(books)

    def search(self):
        field, query = self.view.show_search_menu()
        if field and query:
            results = self.model.search_books(query, field)
            self.view.show_books(results, f"Результаты поиска ({field}): '{query}'")

    def add(self):
        data = self.form_view.input_book_data()
        
        # Проверка на ошибку ввода года в View
        if data.get('year_error'):
            self.view.show_message("Год должен быть числом!", False)
            return

        try:
            new_id = self.model.add_book(
                title=data.get('title', ''),
                author=data.get('author', ''),
                year=data.get('year', 2026),
                genre=data.get('genre', '')
            )
            self.view.show_message(f"Книга добавлена с ID: {new_id}", True)
        except BookValidationError as e:
            self.view.show_message(str(e), False)

    def edit(self):
        book_id = self.form_view.input_book_id()
        if book_id is None:
            return

        try:
            book = self.model.get_book(book_id)
            self.view.show_header("Информация о книге")
            # Простой вывод деталей (можно вынести в отдельный метод view)
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}")
            
            if not self.form_view.confirm("\nРедактировать эту книгу?"):
                return

            data = self.form_view.input_book_data(existing_book=book)
            
            if data.get('year_error'):
                self.view.show_message("Год должен быть числом!", False)
                return

            # Передаем только измененные поля или все (модель сама разберется)
            self.model.update_book(
                book_id=book_id,
                title=data.get('title'),
                author=data.get('author'),
                year=data.get('year'),
                genre=data.get('genre')
            )
            self.view.show_message("Книга успешно обновлена", True)
            
        except BookNotFoundError as e:
            self.view.show_message(str(e), False)
        except BookValidationError as e:
            self.view.show_message(str(e), False)

    def delete(self):
        book_id = self.form_view.input_book_id()
        if book_id is None:
            return

        try:
            book = self.model.get_book(book_id)
            # Показать детали перед удалением
            print(f"Удаление: {book['title']} ({book['author']})")
            
            if not self.form_view.confirm("Вы уверены?"):
                return

            self.model.delete_book(book_id)
            self.view.show_message("Книга удалена", True)
            
        except BookNotFoundError as e:
            self.view.show_message(str(e), False)
        except BookValidationError as e:
            self.view.show_message(str(e), False)

    def toggle_status(self):
        book_id = self.form_view.input_book_id()
        if book_id is None:
            return

        try:
            new_status = self.model.toggle_availability(book_id)
            status_text = "доступна" if new_status else "выдана"
            self.view.show_message(f"Статус изменен: книга теперь {status_text}", True)
        except BookNotFoundError as e:
            self.view.show_message(str(e), False)
        except Exception as e:
            self.view.show_message(f"Ошибка: {str(e)}", False)

    def show_stats(self):
        stats = self.model.get_statistics()
        self.view.show_statistics(stats)