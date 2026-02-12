import psycopg2

conn = psycopg2.connect(
        dbname="db_for_tasks",
        user="postgres",
        password="123",
        host="localhost",
        port=5432
)

cursor = conn.cursor()

cursor.execute("""
    INSERT INTO categories (name) VALUES 
    ('Супы'), 
    ('Салаты'), 
    ('Десерты')
    RETURNING id;
""")

# Добавляем рецепты
cursor.execute("""
    INSERT INTO recipes (name, description, category_id, level) VALUES 
    ('Борщ', 'Классический украинский борщ', 1, 'medium'),
    ('Цезарь', 'Салат с курицей и соусом', 2, 'easy'),
    ('Наполеон', 'Торт с заварным кремом', 3, 'hard')
    RETURNING *;
""")

# Добавляем ингредиенты
cursor.execute("""
    INSERT INTO ingredients (name, description) VALUES 
    ('Свекла', 'Красная корнеплод'),
    ('Курица', 'Куриное филе'),
    ('Мука', 'Пшеничная мука')
    RETURNING *;
""")


conn.commit()
cursor.close()
conn.close()