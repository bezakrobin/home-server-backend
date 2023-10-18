import sqlite3
from flask import jsonify


def get_all_services():
    conn = None
    try:
        conn = sqlite3.connect('db/db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM services')
        services = cursor.fetchall()

        services_list = []
        print(services)
        for service in services:
            services_list.append({
                'id': service[0],
                'name': service[1],
                'svg_data': service[2],
                'active': bool(service[3]),
                'created': service[4],
            })

        return jsonify({'services': services_list})
    except Exception as e:
        print(f"Error getting all services: {str(e)}")
        return jsonify({'error': 'Failed to retrieve services'}), 500
    finally:
        if conn:
            conn.close()
