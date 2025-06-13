
from flask import Flask
from backend_routes_main import main_bp

app = Flask(__name__, template_folder="frontend_templates", static_folder="frontend_static")
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
