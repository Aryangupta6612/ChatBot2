import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

# Load environment variables from .env file
load_dotenv()

GENAI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GENAI_API_KEY:
    raise ValueError("Gemini API key not found. Please check your .env file.")

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)

# Initialize the Flask app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    response = get_chat_response(msg)
    return response

def get_chat_response(text):
    try:
        response = genai.GenerativeModel("gemini-1.5-pro-latest").generate_content([text])
        return response.text if response else "I'm sorry, I couldn't generate a response."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
