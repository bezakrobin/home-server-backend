import sqlite3
from flask import jsonify


def get_service(service_id):
    conn = None
    try:
        conn = sqlite3.connect('db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM services WHERE id = ?', (service_id,))
        service = cursor.fetchone()

        if service:
            return jsonify({'service': service})
        else:
            return jsonify({'error': 'Service not found'}), 404
    except Exception as e:
        print(f"Error retrieving service: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500
    finally:
        if conn:
            conn.close()
