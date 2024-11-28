from flask import Flask, jsonify
from flask_cors import CORS
from .config import Config

def create_app():
    """
    Application factory for creating the Flask app instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS for cross-origin requests
    CORS(app)
    
    # Import and register Blueprints
    from .routes.webhook_routes import webhook_bp  # Ensure this matches your `routes/webhook_routes.py`
    app.register_blueprint(webhook_bp, url_prefix='/api')  # Prefix API endpoints with '/api'
    
    # Default route for health check
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"status": "active", "message": "Zoho SalesIQ Chatbot is running"}), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Resource not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500
    
    return app

# Create and expose the app object for Gunicorn
app = create_app()
