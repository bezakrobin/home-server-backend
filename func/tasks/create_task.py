import sqlite3
from flask import request, jsonify


def create_task():
    conn = None
    try:
        conn = sqlite3.connect('db/db.db')
        cursor = conn.cursor()

        task_data = request.get_json()

        earner_id = task_data.get('earner_id', None)
        name = task_data.get('name', '')
        subtasks = task_data.get('subtasks', [])

        cursor.execute('INSERT INTO tasks (earner_id, name, subtasks) VALUES (?, ?, ?)', (earner_id, name, subtasks))
        conn.commit()

        return jsonify({'message': 'Task created'})
    except Exception as e:
        print(f"Error creating task: {str(e)}")
        return jsonify({'error': 'Failed to create task'}), 500
    finally:
        if conn:
            conn.close()
