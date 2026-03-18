from data.db import Database
from typing import List, Dict, Optional

class BookValidationError(Exception):
    pass

class BookNotFoundError(Exception):
    pass

class BookModel:
    CURRENT_YEAR = 2026

    def __init__(self, db: Database):
        self.db = db

    def _validate_book_data(self, title: str, author: str, year: int, genre: str = ""):
        if not title or not title.strip():
            raise BookValidationError("Название не может быть пустым")
        if len(title.strip()) > 200:
            raise BookValidationError("Название слишком длинное (макс. 200 символов)")
        
        if not author or not author.strip():
            raise BookValidationError("Автор не может быть пустым")
        if len(author.strip()) > 100:
            raise BookValidationError("Имя автора слишком длинное (макс. 100 символов)")
        
        if not isinstance(year, int):
            raise BookValidationError("Год должен быть целым числом")
        if year < 0 or year > self.CURRENT_YEAR:
            raise BookValidationError(f"Год должен быть от 0 до {self.CURRENT_YEAR}")
        
        if genre and len(genre.strip()) > 50:
            raise BookValidationError("Жанр слишком длинный (макс. 50 символов)")

    def get_all_books(self) -> List[Dict]:
        return self.db.get_all_books()

    def search_books(self, query: str, search_by: str) -> List[Dict]:
        if not query or not query.strip():
            return []
        
        if search_by == 'author':
            return self.db.get_book_by_author(query)
        elif search_by == 'title':
            return self.db.get_book_by_title(query)
        elif search_by == 'genre': # Добавлена поддержка поиска по жанру
            return self.db.get_book_by_genre(query)
            
        return self.db.get_all_books()

    def add_book(self, title: str, author: str, year: int, genre: str = "") -> int:
        self._validate_book_data(title, author, year, genre)
        try:
            return self.db.add_book(
                title=title.strip(),
                author=author.strip(),
                year=year,
                genre=genre.strip() if genre else "",
                is_available=True
            )
        except Exception as e:
            raise BookValidationError(f"Ошибка БД при добавлении: {str(e)}")

    def get_book(self, book_id: int) -> Dict:
        book = self.db.get_book_by_id(book_id)
        if not book:
            raise BookNotFoundError(f"Книга с ID {book_id} не найдена")
        return book

    def update_book(self, book_id: int, title: Optional[str] = None, 
                    author: Optional[str] = None, year: Optional[int] = None, 
                    genre: Optional[str] = None) -> bool:
        
        existing_book = self.get_book(book_id) # Проверка существования
        
        # Используем старые значения, если новые не переданы
        final_title = title if title is not None else existing_book['title']
        final_author = author if author is not None else existing_book['author']
        final_year = year if year is not None else existing_book['year']
        final_genre = genre if genre is not None else (existing_book['genre'] or "")
        final_status = existing_book['is_available'] # Статус не меняем через update_book обычно

        self._validate_book_data(final_title, final_author, final_year, final_genre)

        try:
            return self.db.update_book(book_id, final_title, final_author, final_year, final_genre, final_status)
        except Exception as e:
            raise BookValidationError(f"Ошибка БД при обновлении: {str(e)}")

    def delete_book(self, book_id: int) -> bool:
        self.get_book(book_id) # Проверка существования
        try:
            return self.db.delete_book(book_id)
        except Exception as e:
            raise BookValidationError(f"Ошибка БД при удалении: {str(e)}")

    def toggle_availability(self, book_id: int) -> bool:
        self.get_book(book_id) # Проверка существования
        new_status = self.db.toggle_availability(book_id)
        if new_status is None:
            raise BookNotFoundError("Не удалось переключить статус")
        return new_status

    def get_statistics(self) -> Dict[str, int]:
        return self.db.get_statistics()