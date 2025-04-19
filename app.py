import os
from dotenv import load_dotenv
import pytesseract
print(pytesseract.get_tesseract_version())


load_dotenv()
print("OCR_AGENT =", os.getenv("OCR_AGENT"))

from flask import Flask, request, jsonify
from embed import embed
from query import query
from get_vector_db import get_vector_db

TEMP_FOLDER = os.getenv('TEMP_FOLDER', './_temp')
os.makedirs(TEMP_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Server is up"}), 200


@app.route('/embed', methods=['POST'])
def route_embed():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    embedded = embed(file)

    if embedded:
        return jsonify({"message": "File embedded successfully"}), 200

    return jsonify({"error": "File embedded unsuccessfully"}), 400

@app.route('/query', methods=['POST'])
def route_query():
    data = request.get_json()
    response = query(data.get('query'))

    if response:
        return jsonify({"message": response}), 200

    return jsonify({"error": "Something went wrong"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
