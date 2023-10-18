import sqlite3


def init_database(database_name='db/db.db'):
    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()

        create_earners_table_sql = '''
            CREATE TABLE IF NOT EXISTS earners (
                id INTEGER PRIMARY KEY,
                name TEXT,
                svg_data TEXT,
                active BOOLEAN DEFAULT 0,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        '''

        cursor.execute(create_earners_table_sql)

        create_tasks_table_sql = '''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                earner_id INTEGER,
                name TEXT,
                subtasks JSON,
                active BOOLEAN DEFAULT 0,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                finished TIMESTAMP DEFAULT NULL,
                status TEXT DEFAULT NULL
            )
        '''

        cursor.execute(create_tasks_table_sql)
