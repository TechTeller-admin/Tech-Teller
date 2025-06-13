from flask import Flask, render_template
from backend_routes_main import main_bp

app = Flask(__name__, template_folder='frontend_templates', static_folder='frontend_static')
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(debug=True)
