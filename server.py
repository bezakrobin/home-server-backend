from flask import Flask
from routes.earners import earners_bp
from routes.tasks import tasks_bp
from db.initdb import init_database

app = Flask(__name__)

app.register_blueprint(earners_bp)
app.register_blueprint(tasks_bp)

if __name__ == '__main__':
    init_database()
    app.run(debug=True)
