from flask import Flask
from app.routes import chatbot_bp

app = Flask(__name__)

# Daftarkan Blueprint chatbot
app.register_blueprint(chatbot_bp)

if __name__ == "__main__":
    app.run(debug=True)
