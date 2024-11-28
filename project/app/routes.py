from flask import Blueprint, request, jsonify, current_app
from .utils import ChatManager
from functools import wraps
import json

webhook_bp = Blueprint('webhook', __name__)

def verify_zoho_webhook(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_token = request.headers.get('X-ZohoSalesIQ-Auth-Token')
        if not auth_token or auth_token != current_app.config['ZOHO_SALESIQ_AUTH_TOKEN']:
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function

@webhook_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0'
    })

@webhook_bp.route('/webhook', methods=['POST'])
@verify_zoho_webhook
def handle_webhook():
    data = request.json
    chat_manager = ChatManager(current_app.config)
    
    try:
        # Extract message and user data from Zoho SalesIQ payload
        message = data.get('message', {}).get('content')
        user_data = {
            'visitor_id': data.get('visitor', {}).get('id'),
            'name': data.get('visitor', {}).get('name'),
            'email': data.get('visitor', {}).get('email')
        }
        
        # Process message and generate response
        result = chat_manager.handle_message(message, user_data)
        
        # Send response back to Zoho SalesIQ
        response = {
            'message': result['response'],
            'type': 'text'
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500