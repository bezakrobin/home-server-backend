import sqlite3
from flask import jsonify


def delete_earner(earner_id):
    conn = None
    try:
        conn = sqlite3.connect('../../db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM earners WHERE id = ?', (earner_id,))
        existing_earner = cursor.fetchone()

        if not existing_earner:
            return jsonify({'error': 'Earner not found'}), 404

        cursor.execute('DELETE FROM earners WHERE id = ?', (earner_id,))
        conn.commit()

        return jsonify({'message': f'Earner with ID {earner_id} deleted'})
    except Exception as e:
        print(f"Error deleting earner: {str(e)}")
        return jsonify({'error': 'Failed to delete earner'}), 500
    finally:
        if conn:
            conn.close()