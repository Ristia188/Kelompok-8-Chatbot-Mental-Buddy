from flask import Blueprint, request, jsonify, render_template
from app.chatbot import get_response

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")  # Menampilkan halaman HTML yang disediakan

@chatbot_bp.route("/chat", methods=["POST"])
def process_message():
    data = request.get_json()
    user_input = data.get('message', '')
    
    print(f"User input: {user_input}")
    response = get_response(user_input)
    
    print(f"Response: {response}")
    return jsonify(response)
