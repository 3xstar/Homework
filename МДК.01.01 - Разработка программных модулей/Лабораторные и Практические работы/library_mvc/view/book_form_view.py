from view.base_view import BaseView
from typing import Optional, Dict, Any

class BookFormView(BaseView):
    def input_book_data(self, existing_book: Optional[Dict] = None) -> Dict[str, Any]:
        mode = "Редактирование" if existing_book else "Добавление"
        self.show_header(f"{mode} книги")
        
        if existing_book:
            print("(Оставьте поле пустым, чтобы сохранить текущее значение)")
        
        title = input(f"Название ({existing_book['title'] if existing_book else ''}): ")
        author = input(f"Автор ({existing_book['author'] if existing_book else ''}): ")
        year_str = input(f"Год ({existing_book['year'] if existing_book else ''}): ")
        genre = input(f"Жанр ({existing_book.get('genre', '') if existing_book else ''}): ")
        
        result = {}
        
        if title.strip():
            result['title'] = title.strip()
        elif not existing_book:
            result['title'] = "" 
            
        if author.strip():
            result['author'] = author.strip()
        elif not existing_book:
            result['author'] = ""

        if year_str.strip():
            try:
                result['year'] = int(year_str)
            except ValueError:
                result['year_error'] = True 
        elif not existing_book:
            from model.book_model import BookModel
            result['year'] = BookModel.CURRENT_YEAR

        # Явно сохраняем жанр, даже если он пустой (для обновления)
        if genre is not None: 
            result['genre'] = genre.strip()
            
        return result

    def input_book_id(self, prompt: str = "Введите ID книги: ") -> Optional[int]:
        try:
            val = input(prompt)
            if not val.strip():
                return None
            return int(val)
        except ValueError:
            return None