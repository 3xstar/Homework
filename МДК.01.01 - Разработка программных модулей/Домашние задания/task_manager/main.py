import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)


from gui.main_window import main


if __name__ == "__main__":
    print("=" * 40)
    print("Запуск Менеджера задач")
    print("=" * 40)
    
    try:
        from services.task_service import TaskRepository
        repo = TaskRepository()

        test_df = repo.get_all()
        print(f"✓ Подключение к базе данных успешно")
        print(f"✓ Найдено задач: {len(test_df)}")
        print("-" * 40)
        print("Запуск графического интерфейса...")
        print("-" * 40)
        

        main()
        
    except Exception as e:
        print("Ошибка при запуске:")