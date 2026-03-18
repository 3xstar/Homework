import psycopg2
from psycopg2 import sql, extras
from psycopg2.extras import RealDictCursor
from typing import List, Optional, Dict, Any
from contextlib import contextmanager

class Database:
    DEFAULT_CONFIG = {
        'host': 'localhost',
        'port': 5432,
        'database': 'library',
        'user': 'postgres',
        'password': '123'
    }

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = {**self.DEFAULT_CONFIG, **(config or {})}
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = psycopg2.connect(**self.config)
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    @contextmanager
    def cursor(self, dict_cursor=True):
        if not self.connection:
            self.connect()
        cursor_type = RealDictCursor if dict_cursor else psycopg2.cursor
        cursor = self.connection.cursor(cursor_factory=cursor_type)
        try:
            yield cursor
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        finally:
            cursor.close()

    # --- CRUD Operations ---

    def get_all_books(self) -> List[Dict]:
        with self.cursor() as cur:
            cur.execute('SELECT id, title, author, year, genre, is_available FROM books ORDER BY title')
            return cur.fetchall()

    def get_book_by_id(self, book_id: int) -> Optional[Dict]:
        with self.cursor() as cur:
            cur.execute('SELECT id, title, author, year, genre, is_available FROM books WHERE id = %s', (book_id,))
            return cur.fetchone()

    def get_book_by_author(self, author: str) -> List[Dict]:
        with self.cursor() as cur:
            cur.execute('SELECT id, title, author, year, genre, is_available FROM books WHERE author LIKE %s ORDER BY title', (f'%{author}%',))
            return cur.fetchall()

    def get_book_by_title(self, title: str) -> List[Dict]:
        with self.cursor() as cur:
            cur.execute('SELECT id, title, author, year, genre, is_available FROM books WHERE title LIKE %s ORDER BY title', (f"%{title}%",))
            return cur.fetchall()
        
    def get_book_by_genre(self, genre: str) -> List[Dict]:
        with self.cursor() as cur:
            cur.execute(
                'SELECT id, title, author, year, genre, is_available FROM books WHERE genre LIKE %s ORDER BY title', 
                (f'%{genre}%',)
            )
            return cur.fetchall()

    def add_book(self, title: str, author: str, year: int, genre: str = "", is_available: bool = True) -> int:
        with self.cursor() as cur:
            cur.execute(
                'INSERT INTO books(title, author, year, genre, is_available) VALUES(%s, %s, %s, %s, %s) RETURNING id',
                (title, author, year, genre, is_available)
            )
            return cur.fetchone()['id']

    def update_book(self, book_id: int, title: str, author: str, year: int, genre: str, is_available: bool) -> bool:
        with self.cursor() as cur:
            cur.execute(
                'UPDATE books SET title=%s, author=%s, year=%s, genre=%s, is_available=%s WHERE id=%s',
                (title, author, year, genre, is_available, book_id)
            )
            return cur.rowcount > 0

    def delete_book(self, book_id: int) -> bool:
        with self.cursor() as cur:
            cur.execute('DELETE FROM books WHERE id = %s', (book_id,))
            return cur.rowcount > 0

    def toggle_availability(self, book_id: int) -> Optional[bool]:
        book = self.get_book_by_id(book_id)
        if not book:
            return None
        new_status = not book['is_available']
        with self.cursor() as cur:
            cur.execute('UPDATE books SET is_available = %s WHERE id = %s', (new_status, book_id))
            return new_status

    def get_statistics(self) -> Dict[str, int]:
        with self.cursor() as cur:
            cur.execute('SELECT count(*) as total, sum(case when is_available then 1 else 0 end) as available FROM books')
            result = cur.fetchone()
            return {
                'total': result['total'],
                'unavailable': result['total'] - result['available']
            }