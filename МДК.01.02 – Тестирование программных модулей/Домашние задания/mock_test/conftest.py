import pytest
from unittest.mock import Mock, MagicMock
import sys
from pathlib import Path
from repositories.note_repository import NoteRepository
from repositories.category_repository import CategoryRepository
from services.note_service import NoteService
from models.note import Note
from models.category import Category


# Добавляем корень проекта в путь импортов
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# TODO: Импортируйте ваши классы

# ============================================================
# ФИКСТУРЫ ДЛЯ МОКОВ (Unit-тесты)
# ============================================================

@pytest.fixture
def mock_note_repository():
    """
    Фикстура мок-репозитория заметок для unit-тестов

    TODO: Создайте Mock-объект с spec=NoteRepository
    """
    # Ваш код здесь
    # Пример: return Mock(spec=NoteRepository)
    return Mock(spec=NoteRepository)


@pytest.fixture
def mock_category_repository():
    """
    Фикстура мок-репозитория категорий для unit-тестов

    TODO: Создайте Mock-объект с spec=CategoryRepository
    """
    # Ваш код здесь
    return Mock(spec=CategoryRepository)


@pytest.fixture
def note_service(mock_note_repository, mock_category_repository):
    """
    Фикстура сервиса с мок-репозиториями

    TODO: Создайте NoteService и передайте мок-репозитории
    """
    # Ваш код здесь
    return NoteService(mock_note_repository, mock_category_repository)

# ============================================================
# ФИКСТУРЫ С ТЕСТОВЫМИ ДАННЫМИ
# ============================================================

@pytest.fixture
def sample_note():
    """
    Фикстура с тестовой заметкой

    TODO: Создайте объект Note с тестовыми данными
    """
    # Ваш код здесь
    # Пример: return Note(id=1, title="Тест", content="Описание", category_id=1, user_id=1)
    return Note(id=1, title = "Тест", content = "Описание", category_id=1, user_id=1)


@pytest.fixture
def sample_category():
    """
    Фикстура с тестовой категорией

    TODO: Создайте объект Category с тестовыми данными
    """
    # Ваш код здесь
    return Category(1, "Тесты")


@pytest.fixture
def list_of_notes():
    """
    Фикстура со списком заметок

    TODO: Верните список из 2-3 тестовых заметок
    """
    notes_list = [Note(id=2, title = "Тест2", content = "Описание2", category_id=2, user_id=2),
                  Note(id=3, title = "Тест3", content = "Описание3", category_id=3, user_id=3)]
    
    return notes_list

def test_create_note_calls_repository_correctly(note_service, mock_note_repository, sample_note):
    # 1. Настраиваем поведение мок-репозитория
    mock_note_repository.create.return_value = sample_note

    # 2. Вызываем метод сервиса
    result = note_service.create_note(sample_note)

    # 3. Проверяем, что метод репозитория был вызван
    mock_note_repository.create.assert_called_once()

    # 4. Проверяем аргументы вызова
    mock_note_repository.create.assert_called_once_with(sample_note)

    # 5. Проверяем количество вызовов (явная проверка)
    assert mock_note_repository.create.call_count == 1

    # 6. Проверяем, что сервис вернул ожидаемый результат
    assert result == sample_note