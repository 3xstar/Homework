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
    CREATE TYPE levels AS ENUM ('easy', 'medium', 'hard');
""")

cursor.execute("""
    create table categories(
        id serial primary key,
        name varchar(45) not null 
    );
""")


cursor.execute("""
    create table ingredients(
        id serial primary key,
        name varchar(100) not null,
        description text
    );
""")


cursor.execute("""
    create table recipes(
        id serial primary key,
        name varchar(100) not null,
        description text,
        category_id integer references categories(id),
        level levels,
        created_at TIMESTAMP default  current_timestamp
    );
""")


cursor.execute("""
    create table recipes_ingredients(
        recipe_id INT not null references recipes(id),
        ingredient_id INT not null references ingredients(id),
        PRIMARY KEY (recipe_id, ingredient_id)
    );
""")


conn.commit()
cursor.close()
conn.close()