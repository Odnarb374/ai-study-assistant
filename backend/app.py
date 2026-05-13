from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

from src.pipeline import run_pipeline

app = Flask(__name__)
CORS(app)  # allows frontend to connect

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():

    text = request.form.get("text")
    file = request.files.get("file")

    file_path = None

    # Save file if provided
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

    # Run pipeline
    result = run_pipeline(
        file_path=file_path,
        text=text
    )

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=3000)