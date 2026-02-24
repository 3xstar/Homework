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

sys.path.append('c:/VSCODE/pyqt/task_manager')
from services.task_service import TaskRepository


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.repo = TaskRepository()
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
        group_box.setStyleSheet("""
            QGroupBox::title {
                color: #2e7d32;
                font-weight: bold;
                font-size: 14px;
            }
        """)
        layout = QVBoxLayout()

        title_label = QLabel("Название:")
        title_label.setStyleSheet("color: black; font-weight: bold;")
        layout.addWidget(title_label)
        
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Введите название задачи")
        self.title_input.setStyleSheet("color: black; background-color: white;")
        layout.addWidget(self.title_input)

        description_label = QLabel("Описание:")
        description_label.setStyleSheet("color: black; font-weight: bold;")
        layout.addWidget(description_label)
        
        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Введите описание задачи")
        self.description_input.setMaximumHeight(100)
        self.description_input.setStyleSheet("color: black; background-color: white;")
        layout.addWidget(self.description_input)

        status_label = QLabel("Статус:")
        status_label.setStyleSheet("color: black; font-weight: bold;")
        layout.addWidget(status_label)
        
        self.status_combo = QComboBox()
        self.status_combo.addItems(["new", "in_progress", "completed"])
        self.status_combo.setStyleSheet("color: black; background-color: white;")
        layout.addWidget(self.status_combo)

        priority_label = QLabel("Приоритет (1 - самый высокий):")
        priority_label.setStyleSheet("color: black; font-weight: bold;")
        layout.addWidget(priority_label)
        
        self.priority_combo = QComboBox()
        self.priority_combo.setStyleSheet("color: black; background-color: white;")
        layout.addWidget(self.priority_combo)

        layout.addSpacing(10)

        add_button = QPushButton("Добавить задачу")
        add_button.clicked.connect(self.add_task)
        add_button.setMinimumHeight(40)
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(add_button)

        self.create_update_section(layout)

        delete_button = QPushButton("Удалить выбранную задачу")
        delete_button.clicked.connect(self.delete_task)
        delete_button.setMinimumHeight(40)
        delete_button.setStyleSheet("""
            QPushButton {
                background-color: #ff6b6b;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #ff5252;
            }
        """)
        layout.addWidget(delete_button)

        refresh_button = QPushButton("Обновить таблицу")
        refresh_button.clicked.connect(self.load_tasks)
        refresh_button.setMinimumHeight(30)
        refresh_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        layout.addWidget(refresh_button)

        group_box.setLayout(layout)
        return group_box
    
    def get_max_priority(self):
        try:
            df = self.repo.get_all()
            if df.empty:
                return 0
            return int(df['priority'].max())
        except Exception as e:
            print(f"Ошибка получения максимального приоритета: {e}")
            return 0

    def create_update_section(self, parent_layout):
        update_group = QGroupBox("Обновить статус задачи")
        update_group.setStyleSheet("""
            QGroupBox::title {
                color: #2e7d32;
                font-weight: bold;
                font-size: 14px;
            }
        """)
        update_layout = QVBoxLayout()

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        self.update_id_input = QLineEdit()
        self.update_id_input.setPlaceholderText("Введите ID задачи")
        self.update_id_input.setStyleSheet("color: black; background-color: white;")
        id_label = QLabel("ID задачи:")
        id_label.setStyleSheet("color: black; font-weight: bold;")
        form_layout.addRow(id_label, self.update_id_input)

        self.new_status_combo = QComboBox()
        self.new_status_combo.addItems(["new", "in_progress", "completed"])
        self.new_status_combo.setStyleSheet("color: black; background-color: white;")
        status_label = QLabel("Новый статус:")
        status_label.setStyleSheet("color: black; font-weight: bold;")
        form_layout.addRow(status_label, self.new_status_combo)

        update_layout.addLayout(form_layout)

        update_button = QPushButton("Обновить статус")
        update_button.clicked.connect(self.update_task_status)
        update_button.setMinimumHeight(35)
        update_button.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
        """)
        update_layout.addWidget(update_button)

        update_group.setLayout(update_layout)
        parent_layout.addWidget(update_group)

    def create_tasks_table(self):
        group_box = QGroupBox("Список задач")
        group_box.setStyleSheet("""
            QGroupBox::title {
                color: #2e7d32;
                font-weight: bold;
                font-size: 14px;
            }
        """)
        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Название", "Описание", "Статус", "Приоритет"])
        
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        
        self.table.itemSelectionChanged.connect(self.on_task_selected)
        
        self.table.setStyleSheet("""
            QTableWidget {
                color: black;
                background-color: white;
                gridline-color: #d0d0d0;
            }
            QTableWidget::item {
                color: black;
                padding: 5px;
            }
        """)

        layout.addWidget(self.table)
        group_box.setLayout(layout)
        return group_box

    def load_tasks(self):
        try:
            df = self.repo.get_all()
            
            if df.empty:
                self.table.setRowCount(0)
                return

            df = df.sort_values('id')
            
            self.table.setRowCount(len(df))
            
            for i, row in df.iterrows():
                id_item = QTableWidgetItem(str(row['id']))
                id_item.setFlags(id_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                id_item.setForeground(QColor(0, 0, 0))
                self.table.setItem(i, 0, id_item)
                
                title_item = QTableWidgetItem(str(row['title']))
                title_item.setFlags(title_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                title_item.setForeground(QColor(0, 0, 0))
                self.table.setItem(i, 1, title_item)
                
                description_item = QTableWidgetItem(str(row['description']) if row['description'] else "")
                description_item.setFlags(description_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                description_item.setForeground(QColor(0, 0, 0))
                self.table.setItem(i, 2, description_item)
                
                status_item = QTableWidgetItem(str(row['status']))
                status_item.setFlags(status_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                status_item.setForeground(QColor(0, 0, 0))
                self.colorize_status(status_item, str(row['status']))
                self.table.setItem(i, 3, status_item)
                
                priority_value = str(row['priority'])
                priority_item = QTableWidgetItem(priority_value)
                priority_item.setFlags(priority_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                priority_item.setForeground(QColor(0, 0, 0))
                
                priority_num = int(row['priority'])
                if priority_num == 1:
                    priority_item.setBackground(QColor(255, 200, 200))
                elif priority_num <= 3:
                    priority_item.setBackground(QColor(255, 230, 200))
                elif priority_num <= 5:
                    priority_item.setBackground(QColor(255, 255, 200))
                else:
                    priority_item.setBackground(QColor(220, 255, 220))
                    
                self.table.setItem(i, 4, priority_item)

        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            print(f"Ошибка загрузки: {error_details}")
            self.show_error("Ошибка загрузки", f"Не удалось загрузить задачи:\n{str(e)}")

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

            if not title:
                self.show_warning("Предупреждение", "Название задачи не может быть пустым")
                return

            self.repo.add(title, description, status, priority)
            
            self.title_input.clear()
            self.description_input.clear()
            self.status_combo.setCurrentIndex(0)
            
            self.update_priority_combo()
            
            self.load_tasks()
            
            QMessageBox.information(self, "Успех", "Задача успешно добавлена")

        except Exception as e:
            self.show_error("Ошибка добавления", f"Не удалось добавить задачу: {str(e)}")

    def update_priority_combo(self):
        max_priority = self.get_max_priority()
        priority_range = list(range(1, max_priority + 2))
        
        current_value = self.priority_combo.currentText()
        
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

            self.repo.update_status(int(task_id), new_status)
            
            self.update_id_input.clear()
            
            self.update_priority_combo()
            
            self.load_tasks()
            
            QMessageBox.information(self, "Успех", "Статус задачи успешно обновлен")

        except Exception as e:
            self.show_error("Ошибка обновления", f"Не удалось обновить статус:\n{str(e)}")

    def delete_task(self):
        try:
            selected_rows = self.table.selectedIndexes()
            if not selected_rows:
                self.show_warning("Предупреждение", "Выберите задачу для удаления")
                return

            row = selected_rows[0].row()
            task_id = int(self.table.item(row, 0).text())
            task_title = self.table.item(row, 1).text()

            reply = QMessageBox.question(
                self, 
                "Подтверждение удаления",
                f"Вы уверены, что хотите удалить задачу:\n'{task_title}' (ID: {task_id})?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if reply == QMessageBox.StandardButton.Yes:
                self.repo.delete(task_id)
                
                if self.update_id_input.text() == str(task_id):
                    self.update_id_input.clear()
                
                self.update_priority_combo()
                
                self.load_tasks()
                
                QMessageBox.information(self, "Успех", "Задача успешно удалена")

        except Exception as e:
            self.show_error("Ошибка удаления", f"Не удалось удалить задачу:\n{str(e)}")

    def show_error(self, title, message):
        QMessageBox.critical(self, title, message)

    def show_warning(self, title, message):
        QMessageBox.warning(self, title, message)

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #cccccc;
                border-radius: 5px;
                margin-top: 15px;
                padding-top: 15px;
                background-color: #ffffff;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px 0 10px;
                background-color: #f0f0f0;
                border-radius: 3px;
            }
            QLabel {
                color: black;
            }
            QLineEdit, QTextEdit, QComboBox {
                color: black;
                background-color: white;
                border: 1px solid #cccccc;
                border-radius: 3px;
                padding: 5px;
                selection-background-color: #4CAF50;
            }
            QComboBox QAbstractItemView {
                color: black;
                background-color: white;
                selection-background-color: #4CAF50;
                selection-color: white;
            }
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()