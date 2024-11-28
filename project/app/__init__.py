from flask import Flask, jsonify
from flask_cors import CORS
from .config import Config
from .routes import webhook_bp  # Ensure this matches your existing `routes.py`

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS
    CORS(app)
    
    # Register Blueprints
    app.register_blueprint(webhook_bp)
    
    # Default route for health check
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Welcome to the Zoho SalesIQ Chatbot! Server is running."}), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Resource not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500
    
    return app
