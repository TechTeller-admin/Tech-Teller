from flask import Flask, render_template
from backend_routes_main import register_routes

app = Flask(__name__, template_folder='templates', static_folder='static')
register_routes(app)

if __name__ == '__main__':
    app.run()
