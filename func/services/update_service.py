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
        svg_data = data.get('svg_data')
        active = data.get('active')

        cursor.execute('UPDATE services SET name=?, subtasks=?, active=? WHERE id = ?',
                       (name, svg_data, active, service_id))
        conn.commit()

        return jsonify({'message': f'Service with ID {service_id} updated'})
    except Exception as e:
        print(f"Error updating service: {str(e)}")
        return jsonify({'error': 'Failed to update service'}), 500
    finally:
        if conn:
            conn.close()
