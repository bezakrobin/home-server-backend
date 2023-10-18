import sqlite3
from flask import request, jsonify


def update_earner(earner_id):
    conn = None
    try:
        conn = sqlite3.connect('../../db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM earners WHERE id = ?', (earner_id,))
        existing_earner = cursor.fetchone()

        if not existing_earner:
            return jsonify({'error': 'Earner not found'}), 404

        data = request.get_json()

        name = data.get('name')
        svg_data = data.get('svg_data')
        active = data.get('active')

        cursor.execute('UPDATE earners SET name=?, svg_data=?, active=? WHERE id = ?',
                       (name, svg_data, active, earner_id))
        conn.commit()

        return jsonify({'message': f'Earner with ID {earner_id} updated'})
    except Exception as e:
        print(f"Error updating earner: {str(e)}")
        return jsonify({'error': 'Failed to update earner'}), 500
    finally:
        if conn:
            conn.close()
