import psycopg2

conn = psycopg2.connect(
        dbname="db_for_tasks",
        user="postgres",
        password="123",
        host="localhost",
        port=5432
)

cursor = conn.cursor()


print("Вывод записей:\n")

print("Категории: ")
cursor.execute("SELECT name from categories")
result = cursor.fetchall()
print(result)

print("Игредиенты: ")
cursor.execute("SELECT name, description from ingredients")
result = cursor.fetchall()
for row in result:
    print(row)

print("Рецепты: ")
cursor.execute("SELECT name, description from recipes")
result = cursor.fetchall()
for row in result:
    print(row)



print("Добавление записей:\n")
print("Добавление записи (категории):")
cursor.execute("""
    INSERT INTO categories(name) VALUES ('Мучные блюда')
    RETURNING id;
""")
category_id = cursor.fetchone()[0]
print(f"Создана категория с ID: {category_id}")


print("Добавление записи (рецепта):")
cursor.execute("""
    INSERT INTO recipes (name, description, category_id, level) VALUES 
    ('Пельмени', 'Традиционные русские пельмени', %s, 'medium')
    RETURNING *;
""", (category_id,))
recipe_result = cursor.fetchone()
print(f"Добавлен рецепт: {recipe_result[1]}")


cursor.execute("""
    INSERT INTO ingredients (name, description) VALUES 
    ('Фарш', 'Свиной/говяжий')
    RETURNING *;
""")
ingredient_result = cursor.fetchone()
print(f"Добавлен ингредиент: {ingredient_result[1]}")



print("Обновление записей:\n")
print("Обновление записи (категории):")
cursor.execute("""
    UPDATE categories
    SET name = 'Деликатесы'
    WHERE id = %s
    RETURNING id, name;
""", (category_id,))
updated_category = cursor.fetchone()
print(f"Обновлена категория: ID={updated_category[0]}, Новое название = {updated_category[1]}")


print("Обновление записи (рецепта):")
cursor.execute("""
    UPDATE recipes
    SET name = 'Бутерброды', description = 'С колбасой и сыром', category_id = 1, level = 'easy'
    WHERE name = 'Пельмени'
    RETURNING id, name, description, category_id, level;
""")
updated_recipe = cursor.fetchone()
if updated_recipe:
    print(f"Обновлен рецепт: {updated_recipe[1]}")
else:
    print("Рецепт 'Пельмени' не найден!")


print("Обновление записи (ингредиента):")
cursor.execute("""
    UPDATE ingredients
    SET name = 'Морковка', description = 'Оранжевый корнеплод'
    WHERE name = 'Свекла'
    RETURNING id, name, description;
""")
updated_ingredient = cursor.fetchone()
if updated_ingredient:
    print(f"Обновлен ингредиент: {updated_ingredient[1]}")
else:
    print("Ингредиент 'Свекла' не найден!")



print("Удаление записей:\n")
print("Удаление записи (категории)")
cursor.execute("""
    DELETE FROM categories
    WHERE name = 'Десерты'
    RETURNING id, name;
""")
deleted_category = cursor.fetchone()
if deleted_category:
    print(f"Удалена категория: {deleted_category[1]}")
else:
    print("Категория 'Десерты' не найдена!")


print("Удаление записи (рецепта)")
cursor.execute("""
    DELETE FROM recipes
    WHERE name = 'Борщ'
    RETURNING id, name;
""")
deleted_recipe = cursor.fetchone()
if deleted_recipe:
    print(f"Удален рецепт: {deleted_recipe[1]}")
else:
    print("Рецепт 'Борщ' не найден!")


print("Удаление записи (ингредиента)")
cursor.execute("""
    DELETE FROM ingredients
    WHERE name = 'Курица'
    RETURNING id, name;
""")
deleted_ingredient = cursor.fetchone()
if deleted_ingredient:
    print(f"Удален ингредиент: {deleted_ingredient[1]}")
else:
    print("Ингредиент 'Курица' не найден!")



conn.commit()
print("\n✅ Все изменения сохранены в БД!")
cursor.close()
conn.close()