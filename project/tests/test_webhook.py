import unittest
from app import create_app
from app.utils import AIEngine, ChatManager

class TestWebhook(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_webhook_authentication(self):
        response = self.client.post('/webhook')
        self.assertEqual(response.status_code, 401)

    def test_message_processing(self):
        ai_engine = AIEngine(self.app.config['MODEL_PATH'])
        result = ai_engine.predict_intent("Hello, I need help")
        self.assertIsNotNone(result)

    def test_sentiment_analysis(self):
        ai_engine = AIEngine(self.app.config['MODEL_PATH'])
        sentiment = ai_engine.analyze_sentiment("I love this product!")
        self.assertIn('label', sentiment)
        self.assertIn('score', sentiment)

    def tearDown(self):
        self.app_context.pop()