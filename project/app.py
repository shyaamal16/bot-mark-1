from app import create_app
import os
import ssl
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()

if __name__ == '__main__':
    try:
        # Get the port from the environment variable (default to 443)
        port = int(os.getenv("PORT", 443))

        # Check for SSL files and configure SSL context if available
        cert_file = os.getenv("SSL_CERT", "cert.pem")
        key_file = os.getenv("SSL_KEY", "key.pem")
        
        if os.path.exists(cert_file) and os.path.exists(key_file):
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            ssl_context.load_cert_chain(cert_file, key_file)
            logger.info(f"SSL context loaded. Starting server on https://0.0.0.0:{port}")
            # Run the Flask app with HTTPS
            app.run(host='0.0.0.0', port=port, ssl_context=ssl_context)
        else:
            logger.warning("SSL certificates not found. Starting server without SSL on http://0.0.0.0:%s", port)
            # Run the Flask app without SSL
            app.run(host='0.0.0.0', port=port)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        raise
