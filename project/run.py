from app import create_app
import ssl
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()

if __name__ == '__main__':
    try:
        # SSL Configuration for HTTPS
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        ssl_context.load_cert_chain('cert.pem', 'key.pem')
        
        logger.info("Starting server on https://127.0.0.1:443")
        # Run the Flask app with HTTPS
        app.run(host='0.0.0.0', port=443, ssl_context=ssl_context, debug=True)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        raise