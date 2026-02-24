import sys
import os

sys.path.append('c:/VSCODE/gui_with_db')

# Подлючаем модули для работы с БД
from services.category_service import CategoryService
from services.recipe_service import RecipeService
# Подключаем виджеты
from ui.control_panel_widget import ControlPanelWidget
from ui.header_widget import HeaderWidget
from ui.recipe_list_widget import RecipeListWidget

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QListWidget, QLineEdit,
    QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QMessageBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox
)

class AddRecipeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Добавление рецепта')
        self.resize(400, 300)
        self.setup_ui()
        self.load_categories()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Название рецепта
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel('Название: '))
        self.name_input = QLineEdit()
        name_layout.addWidget(self.name_input)
        layout.addLayout(name_layout)

        # Описание
        desc_layout = QHBoxLayout()
        desc_layout.addWidget(QLabel('Описание: '))
        self.desc_input = QLineEdit()
        desc_layout.addWidget(self.desc_input)
        layout.addLayout(desc_layout)

        # Уровень сложности
        level_layout = QHBoxLayout()
        level_layout.addWidget(QLabel('Сложность: '))
        self.level_combo = QComboBox()
        self.level_combo.addItems(['enum', 'medium', 'hard', 'unreal'])
        level_layout.addWidget(self.level_combo)
        layout.addLayout(level_layout)

        # Категория
        cat_layout = QHBoxLayout()
        cat_layout.addWidget(QLabel('Категория: '))
        self.category_combo = QComboBox()
        cat_layout.addWidget(self.category_combo)
        layout.addLayout(cat_layout)

        # Кнопки
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)
    
    def load_categories(self):
        categories = CategoryService.get_all()
        for cat in categories:
            self.category_combo.addItem(cat[1], cat[0])

    def get_recipe_data(self):
        category_id = self.category_combo.currentData()
        return {
            'name': self.name_input.text().strip(),
            'description': self.desc_input.text().strip() or None,
            'level': self.level_combo.currentText(),
            'category_id': category_id if category_id else None
        }


class EditRecipeDialog(QDialog):
    def __init__(self, recipe_data, parent=None):
        super().__init__(parent)
        self.recipe_data = recipe_data  # Ожидается кортеж (id, name, description, level, category_name)
        self.recipe_id = recipe_data[0]
        self.setWindowTitle(f'Редактирование рецепта: {recipe_data[1]} (ID: {recipe_data[0]})')
        self.resize(400, 300)
        self.setup_ui()
        self.load_categories()
        self.fill_data()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Показываем ID рецепта (только для информации)
        id_layout = QHBoxLayout()
        id_layout.addWidget(QLabel('ID рецепта: '))
        id_label = QLabel(str(self.recipe_id))
        id_label.setStyleSheet("font-weight: bold; color: gray;")
        id_layout.addWidget(id_label)
        id_layout.addStretch()
        layout.addLayout(id_layout)

        # Название рецепта
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel('Название: '))
        self.name_input = QLineEdit()
        name_layout.addWidget(self.name_input)
        layout.addLayout(name_layout)

        # Описание
        desc_layout = QHBoxLayout()
        desc_layout.addWidget(QLabel('Описание: '))
        self.desc_input = QLineEdit()
        desc_layout.addWidget(self.desc_input)
        layout.addLayout(desc_layout)

        # Уровень сложности
        level_layout = QHBoxLayout()
        level_layout.addWidget(QLabel('Сложность: '))
        self.level_combo = QComboBox()
        self.level_combo.addItems(['enum', 'medium', 'hard', 'unreal'])
        level_layout.addWidget(self.level_combo)
        layout.addLayout(level_layout)

        # Категория
        cat_layout = QHBoxLayout()
        cat_layout.addWidget(QLabel('Категория: '))
        self.category_combo = QComboBox()
        cat_layout.addWidget(self.category_combo)
        layout.addLayout(cat_layout)

        # Кнопки
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)
    
    def load_categories(self):
        categories = CategoryService.get_all()
        for cat in categories:
            self.category_combo.addItem(cat[1], cat[0])
    
    def fill_data(self):
        # Заполняем поля данными рецепта
        self.name_input.setText(self.recipe_data[1])
        if self.recipe_data[2]:  # description
            self.desc_input.setText(self.recipe_data[2])
        
        # Устанавливаем уровень сложности
        level_index = self.level_combo.findText(self.recipe_data[3])
        if level_index >= 0:
            self.level_combo.setCurrentIndex(level_index)
        
        # Находим и устанавливаем категорию
        # Для этого нужно получить ID категории по её имени
        categories = CategoryService.get_all()
        for cat in categories:
            if cat[1] == self.recipe_data[4]:  # сравниваем имена категорий
                cat_index = self.category_combo.findData(cat[0])
                if cat_index >= 0:
                    self.category_combo.setCurrentIndex(cat_index)
                    break

    def get_recipe_data(self):
        category_id = self.category_combo.currentData()
        return {
            'original_name': self.recipe_data[1],  # оригинальное имя для поиска
            'name': self.name_input.text().strip(),
            'description': self.desc_input.text().strip() or None,
            'level': self.level_combo.currentText(),
            'category_id': category_id if category_id else None
        }


class FilterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Фильтр рецептов')
        self.resize(300, 200)
        self.setup_ui()
        self.filter_type = None
        self.filter_value = None

    def setup_ui(self):
        layout = QVBoxLayout()

        # Выбор типа фильтра
        filter_type_layout = QHBoxLayout()
        filter_type_layout.addWidget(QLabel('Тип фильтра: '))
        self.filter_type_combo = QComboBox()
        self.filter_type_combo.addItems(['По ID', 'По уровню сложности', 'Все рецепты'])
        self.filter_type_combo.currentTextChanged.connect(self.on_filter_type_changed)
        filter_type_layout.addWidget(self.filter_type_combo)
        layout.addLayout(filter_type_layout)

        # Поле для ввода значения фильтра
        value_layout = QHBoxLayout()
        value_layout.addWidget(QLabel('Значение: '))
        self.value_input = QLineEdit()
        self.value_input.setPlaceholderText('Введите ID рецепта')
        self.value_input.setEnabled(False)
        value_layout.addWidget(self.value_input)
        layout.addLayout(value_layout)

        # Для уровня сложности можно сделать выпадающий список
        self.level_combo = QComboBox()
        self.level_combo.addItems(['enum', 'medium', 'hard', 'unreal'])
        self.level_combo.setVisible(False)
        layout.addWidget(self.level_combo)

        # Кнопки
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)
    
    def on_filter_type_changed(self, text):
        # Включаем/выключаем поля ввода в зависимости от выбранного фильтра
        if text == 'Все рецепты':
            self.value_input.setEnabled(False)
            self.level_combo.setVisible(False)
            self.value_input.setVisible(True)
        elif text == 'По уровню сложности':
            self.value_input.setVisible(False)
            self.level_combo.setVisible(True)
        else:  # По ID
            self.value_input.setEnabled(True)
            self.value_input.setVisible(True)
            self.level_combo.setVisible(False)
    
    def get_filter_data(self):
        filter_type = self.filter_type_combo.currentText()
        
        if filter_type == 'По ID':
            return {'type': 'id', 'value': self.value_input.text().strip()}
        elif filter_type == 'По уровню сложности':
            return {'type': 'level', 'value': self.level_combo.currentText()}
        else:
            return {'type': 'all', 'value': None}


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Кулинарное меню')
        self.resize(600, 500)  # Увеличил размер для лучшего отображения
        self.current_recipes = []  # Храним текущий список рецептов
        self.selected_recipe_name = None  # Храним название выбранного рецепта
        self.setup_ui()
        self.load_recipes()
    
    def setup_ui(self):
        main_layout = QVBoxLayout()
        self.header = HeaderWidget('Меню виджетов')
        self.recipe_list = RecipeListWidget()
        self.controls = ControlPanelWidget()

        # Подключаем сигналы
        self.recipe_list.recipe_selected.connect(self.on_recipe_selected)
        self.controls.add_clicked.connect(self.on_add_recipe)
        
        # Добавляем дополнительные кнопки на панель управления
        self.setup_control_panel()

        # Добавляем информационную панель для отображения ID выбранного рецепта
        self.setup_info_panel()

        main_layout.addWidget(self.header)
        main_layout.addWidget(self.recipe_list)
        main_layout.addWidget(self.info_panel)
        main_layout.addWidget(self.controls)

        self.setLayout(main_layout)
    
    def setup_info_panel(self):
        """Создание информационной панели"""
        self.info_panel = QGroupBox("Информация о выбранном рецепте")
        info_layout = QHBoxLayout()
        
        self.selected_id_label = QLabel("ID: -")
        self.selected_id_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        
        self.selected_name_label = QLabel("Название: -")
        self.selected_name_label.setStyleSheet("color: #34495e;")
        
        info_layout.addWidget(self.selected_id_label)
        info_layout.addWidget(self.selected_name_label)
        info_layout.addStretch()
        
        self.info_panel.setLayout(info_layout)
        self.info_panel.setVisible(False)  # Скрываем панель, пока ничего не выбрано
    
    def setup_control_panel(self):
        # Добавляем дополнительные кнопки на существующую панель
        self.controls.add_button = QPushButton('➕ Добавить')
        self.controls.edit_button = QPushButton('✏️ Редактировать')
        self.controls.delete_button = QPushButton('🗑️ Удалить')
        self.controls.filter_button = QPushButton('🔍 Фильтр')
        self.controls.refresh_button = QPushButton('🔄 Обновить')

        # Создаем горизонтальный layout для кнопок, если его нет
        if not hasattr(self.controls, 'button_layout'):
            self.controls.button_layout = QHBoxLayout()
            self.controls.button_layout.addWidget(self.controls.add_button)
            self.controls.button_layout.addWidget(self.controls.edit_button)
            self.controls.button_layout.addWidget(self.controls.delete_button)
            self.controls.button_layout.addWidget(self.controls.filter_button)
            self.controls.button_layout.addWidget(self.controls.refresh_button)
            
            # Добавляем layout на панель управления
            if self.controls.layout():
                self.controls.layout().addLayout(self.controls.button_layout)
        else:
            self.controls.button_layout.addWidget(self.controls.add_button)
            self.controls.button_layout.addWidget(self.controls.edit_button)
            self.controls.button_layout.addWidget(self.controls.delete_button)
            self.controls.button_layout.addWidget(self.controls.filter_button)
            self.controls.button_layout.addWidget(self.controls.search_by_id_button)
            self.controls.button_layout.addWidget(self.controls.refresh_button)

        # Подключаем сигналы для новых кнопок
        self.controls.add_button.clicked.connect(self.on_add_recipe)
        self.controls.edit_button.clicked.connect(self.on_edit_recipe)
        self.controls.delete_button.clicked.connect(self.on_delete_recipe)
        self.controls.filter_button.clicked.connect(self.on_filter_recipes)
        self.controls.refresh_button.clicked.connect(self.on_refresh_recipes)

        # Отключаем кнопки редактирования и удаления по умолчанию (пока не выбран рецепт)
        self.controls.edit_button.setEnabled(False)
        self.controls.delete_button.setEnabled(False)
    
    def load_recipes(self):
        self.recipe_list.clear_recipe()  # Чистим
        recipes = RecipeService.get_all()  # Получаем список рецептов
        self.current_recipes = recipes
        
        if not recipes:
            # Если БД пуста, то добавим тестовые данные
            self.add_sample_data()
            recipes = RecipeService.get_all()
            self.current_recipes = recipes
        
        for recipe in recipes:
            category_name = recipe[4] if recipe[4] else 'Без категории'
            # Передаем ID рецепта в add_recipe
            self.recipe_list.add_recipe(recipe[0], recipe[1], category_name)

    # Добавление тестовых данных
    def add_sample_data(self):
        cat_id_1 = CategoryService.add('Супы')
        cat_id_2 = CategoryService.add('Сладости')
        cat_id_3 = CategoryService.add('Мясное')

        # Создание рецептов
        RecipeService.add_recipe('Борщ', cat_id_1, 'medium', 'Украинский борщ')
        RecipeService.add_recipe('Торт "Наполеон"', cat_id_2, 'hard', 'Торт с заварным кремом')
        RecipeService.add_recipe('Индейка', cat_id_3, 'enum', 'Запеченная индейка с овощами')

    def on_recipe_selected(self, name):
        # Сохраняем выбранный рецепт
        self.selected_recipe_name = name
        
        # Находим выбранный рецепт в текущем списке
        selected_recipe = None
        for recipe in self.current_recipes:
            if recipe[1] == name:  # recipe[1] - это название
                selected_recipe = recipe
                break
        
        if selected_recipe:
            # Обновляем информационную панель
            self.selected_id_label.setText(f"ID: {selected_recipe[0]}")
            self.selected_name_label.setText(f"Название: {selected_recipe[1]}")
            self.info_panel.setVisible(True)
            
            # Включаем кнопки редактирования и удаления
            self.controls.edit_button.setEnabled(True)
            self.controls.delete_button.setEnabled(True)
            
            # Показываем подробную информацию
            QMessageBox.information(self, 'Рецепт Выбран', 
                                   f'ID: {selected_recipe[0]}\n'
                                   f'Название: {name}\n'
                                   f'Описание: {selected_recipe[2] or "Нет описания"}\n'
                                   f'Сложность: {selected_recipe[3]}\n'
                                   f'Категория: {selected_recipe[4]}')

    def get_selected_recipe_card(self):
        """Получить выбранную карточку рецепта"""
        if not self.selected_recipe_name:
            return None
        
        # Ищем карточку с нужным названием в layout
        for i in range(self.recipe_list.layout.count()):
            card = self.recipe_list.layout.itemAt(i).widget()
            if card and hasattr(card, 'name') and card.name == self.selected_recipe_name:
                return card
        return None

    def on_add_recipe(self):
        dialog = AddRecipeDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_recipe_data()
            if not data['name']:
                QMessageBox.warning(self, 'Ошибка', 'Введите название рецепта')
                return
            
            recipe_id_result = RecipeService.add_recipe(
                name=data['name'],
                category_id=data['category_id'],
                level=data['level'],
                description=data['description']
            )

            # Проверяем, что recipe_id_result не None и является кортежем/числом
            if recipe_id_result and recipe_id_result[0] > 0:
                recipe_id = recipe_id_result[0]  # Получаем ID из результата
                category_name = 'Без категории'
                if data['category_id']:
                    cat = CategoryService.get_by_id(data['category_id'])
                    category_name = cat[0][1] if cat and len(cat) > 0 else 'Без категории'

                # Передаем ID нового рецепта (теперь 3 аргумента)
                self.recipe_list.add_recipe(recipe_id, data['name'], category_name)
                # Обновляем текущий список рецептов
                self.current_recipes = RecipeService.get_all()
                QMessageBox.information(self, 'Успех', f'Рецепт добавлен! ID: {recipe_id}')
            else:
                QMessageBox.critical(self, 'Ошибка', 'Не удалось добавить рецепт')

    def on_edit_recipe(self):
        # Получаем выбранный рецепт
        if not self.selected_recipe_name:
            QMessageBox.warning(self, 'Ошибка', 'Выберите рецепт для редактирования')
            return
        
        selected_name = self.selected_recipe_name
        
        # Находим полные данные рецепта
        recipe_to_edit = None
        for recipe in self.current_recipes:
            if recipe[1] == selected_name:
                recipe_to_edit = recipe
                break
        
        if not recipe_to_edit:
            QMessageBox.critical(self, 'Ошибка', 'Не удалось найти данные рецепта')
            return
        
        # Открываем диалог редактирования
        dialog = EditRecipeDialog(recipe_to_edit, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_recipe_data()
            if not data['name']:
                QMessageBox.warning(self, 'Ошибка', 'Название рецепта не может быть пустым')
                return
            
            # Вызываем метод редактирования
            result = RecipeService.edit_recipe(
                recipe_name=data['original_name'],
                name=data['name'],
                category_id=data['category_id'],
                level=data['level'],
                description=data['description']
            )
            
            if result:
                # Обновляем отображение
                self.on_refresh_recipes()
                QMessageBox.information(self, 'Успех', 'Рецепт успешно обновлен!')
            else:
                QMessageBox.critical(self, 'Ошибка', 'Не удалось обновить рецепт')

    def on_delete_recipe(self):
        # Получаем выбранный рецепт
        if not self.selected_recipe_name:
            QMessageBox.warning(self, 'Ошибка', 'Выберите рецепт для удаления')
            return
        
        selected_name = self.selected_recipe_name
        
        # Находим ID рецепта
        recipe_id = None
        for recipe in self.current_recipes:
            if recipe[1] == selected_name:
                recipe_id = recipe[0]  # ID рецепта
                break
        
        if not recipe_id:
            QMessageBox.critical(self, 'Ошибка', 'Не удалось найти ID рецепта')
            return
        
        # Подтверждение удаления
        reply = QMessageBox.question(
            self, 
            'Подтверждение удаления',
            f'Вы уверены, что хотите удалить рецепт "{selected_name}" (ID: {recipe_id})?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            # Вызываем метод удаления
            deleted_count = RecipeService.delete_recipe(recipe_id)
            
            if deleted_count and deleted_count > 0:
                # Находим и удаляем карточку из layout
                for i in range(self.recipe_list.layout.count()):
                    card = self.recipe_list.layout.itemAt(i).widget()
                    if card and hasattr(card, 'name') and card.name == selected_name:
                        # Удаляем виджет
                        card.deleteLater()
                        break
                
                # Обновляем текущий список рецептов
                self.current_recipes = RecipeService.get_all()
                
                # Скрываем информационную панель и сбрасываем выбранный рецепт
                self.selected_recipe_name = None
                self.info_panel.setVisible(False)
                
                # Отключаем кнопки, если список пуст
                if self.recipe_list.layout.count() == 0:
                    self.controls.edit_button.setEnabled(False)
                    self.controls.delete_button.setEnabled(False)
                
                QMessageBox.information(self, 'Успех', f'Рецепт (ID: {recipe_id}) успешно удален!')
            else:
                QMessageBox.critical(self, 'Ошибка', 'Не удалось удалить рецепт')

    def on_filter_recipes(self):
        dialog = FilterDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            filter_data = dialog.get_filter_data()
            
            filtered_recipes = []
            
            if filter_data['type'] == 'id':
                # Фильтр по ID
                try:
                    recipe_id = int(filter_data['value'])
                    recipe = RecipeService.get_by_id(recipe_id)
                    if recipe:
                        filtered_recipes = recipe
                except ValueError:
                    QMessageBox.warning(self, 'Ошибка', 'Введите корректный ID (число)')
                    return
                    
            elif filter_data['type'] == 'level':
                # Фильтр по уровню сложности
                filtered_recipes = RecipeService.get_by_level(filter_data['value'])
                
            else:  # 'all'
                # Все рецепты
                filtered_recipes = RecipeService.get_all()
            
            # Обновляем отображение
            self.recipe_list.clear_recipe()
            
            if filtered_recipes:
                # Проверяем, является ли filtered_recipes списком или одним рецептом
                if isinstance(filtered_recipes, list):
                    recipes_to_show = filtered_recipes
                else:
                    recipes_to_show = [filtered_recipes] if filtered_recipes else []
                
                for recipe in recipes_to_show:
                    category_name = recipe[4] if recipe[4] else 'Без категории'
                    # Передаем ID рецепта (теперь 3 аргумента)
                    self.recipe_list.add_recipe(recipe[0], recipe[1], category_name)
                
                # Обновляем текущий список рецептов
                self.current_recipes = recipes_to_show
                
                # Скрываем информационную панель и сбрасываем выбранный рецепт
                self.selected_recipe_name = None
                self.info_panel.setVisible(False)
                self.controls.edit_button.setEnabled(False)
                self.controls.delete_button.setEnabled(False)
                
                QMessageBox.information(
                    self, 
                    'Фильтр применен', 
                    f'Найдено рецептов: {len(recipes_to_show)}'
                )
            else:
                self.current_recipes = []
                self.info_panel.setVisible(False)
                QMessageBox.information(self, 'Фильтр применен', 'Рецепты не найдены')

    def on_refresh_recipes(self):
        # Обновляем список рецептов
        self.load_recipes()
        
        # Скрываем информационную панель и сбрасываем выбранный рецепт
        self.selected_recipe_name = None
        self.info_panel.setVisible(False)
        self.controls.edit_button.setEnabled(False)
        self.controls.delete_button.setEnabled(False)
        
        QMessageBox.information(self, 'Обновление', 'Список рецептов обновлен')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())