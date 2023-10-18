import sqlite3
from flask import jsonify


def activate_service(service_id):
    conn = None
    try:
        conn = sqlite3.connect('db/db.db')
        cursor = conn.cursor()

        cursor.execute(f"UPDATE services SET active = 1 WHERE id = ?", (service_id,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({'message': f'Service with ID {service_id} activated'})
        else:
            return jsonify({'error': 'Service not found'}), 404

    except Exception as e:
        print(f"Error activating service: {str(e)}")
        return jsonify({'error': 'Failed to activate service'}), 500
    finally:
        if conn:
            conn.close()
