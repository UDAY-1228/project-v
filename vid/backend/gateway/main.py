"""
VID API Gateway – Entry Point
"""
import os
from dotenv import load_dotenv
from src.app import create_app

load_dotenv()

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("GATEWAY_PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=app.config.get("DEBUG", False))
