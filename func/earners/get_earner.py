import sqlite3
from flask import jsonify


def get_earner(earner_id):
    conn = None
    try:
        conn = sqlite3.connect('../../db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM earners WHERE id = ?', (earner_id,))
        earner = cursor.fetchone()

        if earner:
            return jsonify({'earner': earner})
        else:
            return jsonify({'error': 'Earner not found'}), 404
    except Exception as e:
        print(f"Error retrieving earner: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500
    finally:
        if conn:
            conn.close()
