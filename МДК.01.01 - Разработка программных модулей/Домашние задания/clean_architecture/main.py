import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from presentation.main_window import main

if __name__ == "__main__":
    print("=" * 40)
    print("Запуск Менеджера задач")
    print("=" * 40)
    print("Запуск графического интерфейса...")
    print("-" * 40)
    main()