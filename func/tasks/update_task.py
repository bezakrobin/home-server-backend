import sqlite3
from flask import jsonify, request


def update_task(task_id):
    conn = None
    try:
        conn = sqlite3.connect('db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM tasks WHERE id = ?', (task_id,))
        existing_task = cursor.fetchone()

        if not existing_task:
            return jsonify({'error': 'Task not found'}), 404

        update_data = request.get_json()

        update_query = 'UPDATE tasks SET '
        update_params = []

        if 'name' in update_data:
            update_query += 'name = ?, '
            update_params.append(update_data['name'])

        if 'subtasks' in update_data:
            update_query += 'subtasks = ?, '
            update_params.append(update_data['subtasks'])

        if 'active' in update_data:
            update_query += 'active = ?, '
            update_params.append(update_data['active'])

        if 'finished' in update_data:
            update_query += 'finished = ?, '
            update_params.append(update_data['finished'])

        if 'status' in update_data:
            update_query += 'status = ?, '
            update_params.append(update_data['status'])

        if 'service_id' in update_data:
            update_query += 'service_id = ?, '
            update_params.append(update_data['service_id'])

        update_query = update_query[:-2] + ' WHERE id = ?'
        update_params.append(task_id)

        cursor.execute(update_query, tuple(update_params))
        conn.commit()

        return jsonify({'message': f'Task with ID {task_id} updated'})
    except Exception as e:
        print(f"Error updating task: {str(e)}")
        return jsonify({'error': 'Failed to update task'}), 500
    finally:
        if conn:
            conn.close()
