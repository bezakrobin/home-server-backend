import sqlite3
from flask import jsonify


def get_all_tasks():
    conn = None
    try:
        conn = sqlite3.connect('db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()

        task_list = []
        for task in tasks:
            task_dict = {
                'id': task[0],
                'service_id': task[1],
                'name': task[2],
                'subtasks': task[3],
                'active': task[4],
                'created': task[5],
                'finished': task[6],
                'status': task[7]
            }
            task_list.append(task_dict)

        return jsonify(task_list)
    except Exception as e:
        print(f"Error retrieving tasks: {str(e)}")
        return jsonify({'error': 'Failed to retrieve tasks'}), 500
    finally:
        if conn:
            conn.close()
