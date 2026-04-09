import sys
import pandas as pd
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QLineEdit,
    QComboBox, QTextEdit, QLabel, QMessageBox, QHeaderView,
    QGroupBox, QFormLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor
from service.task_service import TaskService

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.service = TaskService()  # Только Service, не Repository!
        self.init_ui()
        self.load_tasks()
        self.update_priority_combo()
    
    def init_ui(self):
        self.setWindowTitle("Менеджер задач")
        self.setGeometry(100, 100, 900, 600)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        left_panel = self.create_add_form()
        main_layout.addWidget(left_panel, 1)
        right_panel = self.create_tasks_table()
        main_layout.addWidget(right_panel, 2)
        self.apply_styles()
    
    def create_add_form(self):
        group_box = QGroupBox("Добавить новую задачу")
        layout = QVBoxLayout()
        
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Введите название задачи")
        layout.addWidget(self.title_input)
        
        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Введите описание задачи")
        self.description_input.setMaximumHeight(100)
        layout.addWidget(self.description_input)
        
        self.status_combo = QComboBox()
        self.status_combo.addItems(["new", "in_progress", "completed"])
        layout.addWidget(self.status_combo)
        
        self.priority_combo = QComboBox()
        layout.addWidget(self.priority_combo)
        
        add_button = QPushButton("Добавить задачу")
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)
        
        self.create_update_section(layout)
        
        delete_button = QPushButton("Удалить выбранную задачу")
        delete_button.clicked.connect(self.delete_task)
        layout.addWidget(delete_button)
        
        refresh_button = QPushButton("Обновить таблицу")
        refresh_button.clicked.connect(self.load_tasks)
        layout.addWidget(refresh_button)
        
        group_box.setLayout(layout)
        return group_box
    
    def create_update_section(self, parent_layout):
        update_group = QGroupBox("Обновить статус задачи")
        update_layout = QVBoxLayout()
        form_layout = QFormLayout()
        
        self.update_id_input = QLineEdit()
        self.update_id_input.setPlaceholderText("Введите ID задачи")
        form_layout.addRow(QLabel("ID задачи:"), self.update_id_input)
        
        self.new_status_combo = QComboBox()
        self.new_status_combo.addItems(["new", "in_progress", "completed"])
        form_layout.addRow(QLabel("Новый статус:"), self.new_status_combo)
        
        update_layout.addLayout(form_layout)
        
        update_button = QPushButton("Обновить статус")
        update_button.clicked.connect(self.update_task_status)
        update_layout.addWidget(update_button)
        
        update_group.setLayout(update_layout)
        parent_layout.addWidget(update_group)
    
    def create_tasks_table(self):
        group_box = QGroupBox("Список задач")
        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Название", "Описание", "Статус", "Приоритет"]
        )
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.table.itemSelectionChanged.connect(self.on_task_selected)
        
        layout.addWidget(self.table)
        group_box.setLayout(layout)
        return group_box
    
    def load_tasks(self):
        try:
            df = self.service.get_all_tasks()
            if df.empty:
                self.table.setRowCount(0)
                return
            df = df.sort_values('id')
            self.table.setRowCount(len(df))
            for i, row in df.iterrows():
                self.table.setItem(i, 0, QTableWidgetItem(str(row['id'])))
                self.table.setItem(i, 1, QTableWidgetItem(str(row['title'])))
                self.table.setItem(i, 2, 
                    QTableWidgetItem(str(row['description']) if row['description'] else ""))
                status_item = QTableWidgetItem(str(row['status']))
                self.colorize_status(status_item, str(row['status']))
                self.table.setItem(i, 3, status_item)
                priority_item = QTableWidgetItem(str(row['priority']))
                self.table.setItem(i, 4, priority_item)
        except Exception as e:
            self.show_error("Ошибка загрузки", str(e))
    
    def colorize_status(self, item, status):
        colors = {
            'new': QColor(255, 255, 200),
            'in_progress': QColor(200, 230, 255),
            'completed': QColor(200, 255, 200)
        }
        if status in colors:
            item.setBackground(colors[status])
    
    def on_task_selected(self):
        selected_rows = self.table.selectedIndexes()
        if selected_rows:
            row = selected_rows[0].row()
            task_id = self.table.item(row, 0).text()
            self.update_id_input.setText(task_id)
    
    def add_task(self):
        try:
            title = self.title_input.text().strip()
            description = self.description_input.toPlainText().strip()
            status = self.status_combo.currentText()
            priority = int(self.priority_combo.currentText())
            
            # Валидация делегирована в Service
            self.service.create_task(title, description, status, priority)
            
            self.title_input.clear()
            self.description_input.clear()
            self.status_combo.setCurrentIndex(0)
            self.update_priority_combo()
            self.load_tasks()
            QMessageBox.information(self, "Успех", "Задача успешно добавлена")
        except ValueError as e:
            self.show_warning("Предупреждение", str(e))
        except Exception as e:
            self.show_error("Ошибка добавления", str(e))
    
    def update_priority_combo(self):
        max_priority = self.service.get_max_priority()
        priority_range = list(range(1, max_priority + 2))
        self.priority_combo.clear()
        self.priority_combo.addItems([str(p) for p in priority_range])
        self.priority_combo.setCurrentText(str(max_priority + 1))
    
    def update_task_status(self):
        try:
            task_id = self.update_id_input.text().strip()
            new_status = self.new_status_combo.currentText()
            
            if not task_id:
                self.show_warning("Предупреждение", "Введите ID задачи")
                return
            if not task_id.isdigit():
                self.show_warning("Предупреждение", "ID задачи должен быть числом")
                return
            
            # Валидация делегирована в Service
            self.service.change_status(int(task_id), new_status)
            
            self.update_id_input.clear()
            self.update_priority_combo()
            self.load_tasks()
            QMessageBox.information(self, "Успех", "Статус обновлён")
        except ValueError as e:
            self.show_warning("Предупреждение", str(e))
        except Exception as e:
            self.show_error("Ошибка обновления", str(e))
    
    def delete_task(self):
        try:
            selected_rows = self.table.selectedIndexes()
            if not selected_rows:
                self.show_warning("Предупреждение", "Выберите задачу")
                return
            row = selected_rows[0].row()
            task_id = int(self.table.item(row, 0).text())
            task_title = self.table.item(row, 1).text()
            
            reply = QMessageBox.question(
                self, "Подтверждение удаления",
                f"Удалить задачу: '{task_title}' (ID: {task_id})?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.service.remove_task(task_id)
                if self.update_id_input.text() == str(task_id):
                    self.update_id_input.clear()
                self.update_priority_combo()
                self.load_tasks()
                QMessageBox.information(self, "Успех", "Задача удалена")
        except ValueError as e:
            self.show_warning("Предупреждение", str(e))
        except Exception as e:
            self.show_error("Ошибка удаления", str(e))
    
    def show_error(self, title, message):
        QMessageBox.critical(self, title, message)
    
    def show_warning(self, title, message):
        QMessageBox.warning(self, title, message)
    
    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #f0f0f0; }
            QGroupBox { 
                font-weight: bold; border: 2px solid #cccccc;
                border-radius: 5px; margin-top: 15px; padding-top: 15px;
                background-color: #ffffff;
            }
            QLineEdit, QTextEdit, QComboBox {
                color: black; background-color: white;
                border: 1px solid #cccccc; border-radius: 3px; padding: 5px;
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())