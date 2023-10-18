import sqlite3
from flask import jsonify


def disable_task(task_id):
    conn = None
    try:
        conn = sqlite3.connect('../db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM tasks WHERE id = ?', (task_id,))
        existing_task = cursor.fetchone()

        if not existing_task:
            return jsonify({'error': 'Task not found'}), 404

        cursor.execute('UPDATE tasks SET active = 0 WHERE id = ?', (task_id,))
        conn.commit()

        return jsonify({'message': f'Task with ID {task_id} disabled'})
    except Exception as e:
        print(f"Error disabling task: {str(e)}")
        return jsonify({'error': 'Failed to disable task'}), 500
    finally:
        if conn:
            conn.close()
