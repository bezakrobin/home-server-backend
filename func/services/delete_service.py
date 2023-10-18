import sqlite3
from flask import jsonify


def delete_service(service_id):
    conn = None
    try:
        conn = sqlite3.connect('db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM services WHERE id = ?', (service_id,))
        existing_service = cursor.fetchone()

        if not existing_service:
            return jsonify({'error': 'Service not found'}), 404

        cursor.execute('DELETE FROM services WHERE id = ?', (service_id,))
        conn.commit()

        return jsonify({'message': f'Service with ID {service_id} deleted'})
    except Exception as e:
        print(f"Error deleting service: {str(e)}")
        return jsonify({'error': 'Failed to delete service'}), 500
    finally:
        if conn:
            conn.close()
