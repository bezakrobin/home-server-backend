import sqlite3
from flask import jsonify


def delete_task(task_id):
    conn = None
    try:
        conn = sqlite3.connect('db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM tasks WHERE id = ?', (task_id,))
        existing_task = cursor.fetchone()

        if not existing_task:
            return jsonify({'error': 'Task not found'}), 404

        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()

        return jsonify({'message': f'Task with ID {task_id} deleted'})
    except Exception as e:
        print(f"Error deleting task: {str(e)}")
        return jsonify({'error': 'Failed to delete task'}), 500
    finally:
        if conn:
            conn.close()
