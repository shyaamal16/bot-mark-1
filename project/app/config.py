import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    ZOHO_SALESIQ_AUTH_TOKEN = os.getenv('ZOHO_SALESIQ_AUTH_TOKEN')
    ZOHO_SALESIQ_PORTAL_ID = os.getenv('ZOHO_SALESIQ_PORTAL_ID')
    ZOHO_SALESIQ_DEPARTMENT_ID = os.getenv('ZOHO_SALESIQ_DEPARTMENT_ID')
    
    # AI Model Configuration
    MODEL_PATH = 'app/models/chatbot_model'
    INTENT_THRESHOLD = 0.7
    
    # Integration Settings
    ZOHO_CRM_API_URL = os.getenv('ZOHO_CRM_API_URL')
    ZOHO_DESK_API_URL = os.getenv('ZOHO_DESK_API_URL')
    
    # Feature Flags
    ENABLE_TRANSLATION = True
    ENABLE_SENTIMENT_ANALYSIS = True
    ENABLE_GAMIFICATION = True