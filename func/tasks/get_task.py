import sqlite3
from flask import jsonify


def get_task(task_id):
    conn = None
    try:
        conn = sqlite3.connect('../db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()

        if task:
            task_dict = {
                'id': task[0],
                'earner_id': task[1],
                'name': task[2],
                'subtasks': task[3],
                'active': task[4],
                'created': task[5],
                'finished': task[6],
                'status': task[7]
            }
            return jsonify(task_dict)
        else:
            return jsonify({'error': 'Task not found'}), 404
    except Exception as e:
        print(f"Error retrieving task: {str(e)}")
        return jsonify({'error': 'Failed to retrieve task'}), 500
    finally:
        if conn:
            conn.close()
