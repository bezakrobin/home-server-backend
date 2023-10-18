import sqlite3
from flask import jsonify


def get_all_earners():
    conn = None
    try:
        conn = sqlite3.connect('../../db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM earners')
        earners = cursor.fetchall()

        earners_list = []
        for earner in earners:
            earners_list.append({
                'id': earner[0],
                'name': earner[1],
                'svg_data': earner[2],
                'active': bool(earner[3])
            })

        return jsonify({'earners': earners_list})
    except Exception as e:
        print(f"Error getting all earners: {str(e)}")
        return jsonify({'error': 'Failed to retrieve earners'}), 500
    finally:
        if conn:
            conn.close()
