# Карточка рецепта

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import pyqtSignal

class RecipeCardWidget(QWidget):
    selected = pyqtSignal(str)

    def __init__(self, recipe_id, name, category):
        super().__init__()
        self.recipe_id = recipe_id  # Сохраняем ID рецепта
        self.name = name  # Сохраняем название для сигнала
        
        layout = QHBoxLayout()
        
        # Отображаем ID рецепта
        id_label = QLabel(f"ID: {recipe_id}")
        id_label.setStyleSheet("color: gray; font-size: 10px; min-width: 50px;")
        layout.addWidget(id_label)
        
        # Название рецепта
        name_label = QLabel(name)
        name_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(name_label)
        
        # Категория
        category_label = QLabel(f"({category})")
        category_label.setStyleSheet("color: blue;")
        layout.addWidget(category_label)
        
        # Кнопка просмотра
        view_button = QPushButton("👁️")
        view_button.setMaximumWidth(30)
        view_button.clicked.connect(self.on_view_clicked)
        layout.addWidget(view_button)
        
        # Добавляем растяжение, чтобы элементы не прижимались влево
        layout.addStretch()
        
        self.setLayout(layout)
    
    def on_view_clicked(self):
        self.selected.emit(self.name)