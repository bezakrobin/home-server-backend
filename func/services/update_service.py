import sqlite3
from flask import request, jsonify


def update_service(service_id):
    conn = None
    try:
        conn = sqlite3.connect('db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM services WHERE id = ?', (service_id,))
        existing_service = cursor.fetchone()

        if not existing_service:
            return jsonify({'error': 'Service not found'}), 404

        data = request.get_json()

        name = data.get('name')
        subtasks = data.get('subtasks')
        active = data.get('active')
        finished = data.get('finished')
        status = data.get('status')

        cursor.execute('UPDATE services SET name=?, subtasks=?, active=?, finished=?, status=? WHERE id = ?',
                       (name, subtasks, active, finished, status, service_id))
        conn.commit()

        return jsonify({'message': f'Service with ID {service_id} updated'})
    except Exception as e:
        print(f"Error updating service: {str(e)}")
        return jsonify({'error': 'Failed to update service'}), 500
    finally:
        if conn:
            conn.close()
