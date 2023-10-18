import sqlite3
from flask import request, jsonify


def create_service():
    conn = None
    try:
        data = request.get_json()

        name = data.get('name')
        svg_data = data.get('svg_data')

        conn = sqlite3.connect('db/db.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO services (name, svg_data) VALUES (?, ?)', (name, svg_data))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Service created'}), 200
    except Exception as e:
        print(f"Error creating service: {str(e)}")
        return jsonify({'error': 'Failed to create service'}), 500
    finally:
        if conn:
            conn.close()
