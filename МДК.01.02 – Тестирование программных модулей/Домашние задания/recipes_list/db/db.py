import psycopg2 # Подключение к БД

# Создание подключения
def get_conn():
        return psycopg2.connect(
                host='localhost', 
                port=5432,
                user='postgres',
                password='123',
                database='recipe_db'
        )

'''
Пример

def get_conn():
    return psycopg2.connect(
    host='localhost',
    port=5432,
    user='postgres',
    password='password',
    database='db_name',
    client_encoding='utf=8')
'''