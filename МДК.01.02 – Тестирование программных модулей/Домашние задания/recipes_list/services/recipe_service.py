# Работа с таблицей "recipes"
import db.db as db
import sys
import os

sys.path.append('c:/VSCODE/gui_with_db')

class RecipeService:
        @staticmethod
        def get_all():
                try:
                        conn = db.get_conn()
                        cursor = conn.cursor()
                        cursor.execute('''
                        select r.id, r.name, r.description, r.level, c.name from recipes.recipes r join recipes.categories c on r.category_id = c.id; 
                        ''')
                        result = cursor.fetchall() # Преобразуем данные в кортеж
                        cursor.close()
                        conn.close()
                        return result
                except:
                        print('Ошибка')
                        raise
        
        @staticmethod
        def get_by_id(recipe_id):
                try:
                        conn = db.get_conn()
                        cursor = conn.cursor()
                        cursor.execute('''
                        select r.id, r.name, r.description, r.level, c.name from recipes.recipes r join recipes.categories c on r.category_id = c.id WHERE r.id = %s; 
                        ''', (recipe_id, ))
                        result = cursor.fetchall() # Преобразуем данные в кортеж
                        cursor.close()
                        conn.close()
                except:
                        print('Ошибка в запросе')
                return result

        @staticmethod
        def get_by_level(recipe_level):
                try:
                        conn = db.get_conn()
                        cursor = conn.cursor()
                        cursor.execute('''
                        select r.id, r.name, r.description, r.level, c.name from recipes.recipes r join recipes.categories c on r.category_id = c.id WHERE r.level = %s; 
                        ''', (recipe_level, ))
                        result = cursor.fetchall() # Преобразуем данные в кортеж
                        cursor.close()
                        conn.close()
                except:
                        print('Ошибка в запросе')
                return result

        @staticmethod
        # Добавление рецепта
        def add_recipe(name, category_id, level, description=None):
                try:
                        conn = db.get_conn()
                        cursor = conn.cursor()
                        cursor.execute('''
                        INSERT INTO recipes.recipes (name, description, level, category_id) VALUES(%s, %s, %s, %s) RETURNING id 
                        ''', (name, description, level, category_id))
                        result = cursor.fetchall()[0] # Просмотр добавленого элемента
                        print(type(result))
                        conn.commit()
                        cursor.close()
                        conn.close()
                except:
                        conn.rollback()
                        print('Ошибка в запросе')
                return result
        
        @staticmethod
        # Удаление рецепта
        def delete_recipe(id):
                try:
                        conn = db.get_conn()
                        cursor = conn.cursor()
                        cursor.execute('''
                        DELETE FROM recipes.recipes WHERE id = %s
                        ''', (id,))
                        deleted_count = cursor.rowcount

                        if deleted_count > 0:
                                print(f"Элемент под id = {id} успешно удален")
                        else:
                                print(f"Элемент с id = {id} не найден")
                        conn.commit()
                        cursor.close()
                        conn.close()
                except:
                        conn.rollback()
                        print('Ошибка в запросе')
                return deleted_count
        
        @staticmethod
        # Редактирование рецепта
        def edit_recipe(recipe_name, name, category_id, level, description=None):
                try:
                        conn = db.get_conn()
                        cursor = conn.cursor()
                        cursor.execute('''
                        UPDATE recipes.recipes
                        SET name = %s, category_id = %s, level = %s, description = %s
                        WHERE name = %s
                        RETURNING id
                        ''', (name, category_id, level, description, recipe_name))
                        result = cursor.fetchone()
                        print("Изменненый элемент: ", result)
                        conn.commit()
                        cursor.close()
                        conn.close()
                except:
                        conn.rollback()
                        print('Ошибка в запросе')
                return result
