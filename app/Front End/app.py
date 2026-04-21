from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Check for pdf/txt files
ALLOWED_FILES = {'pdf', 'txt'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILES

@app.route('/', methods=['GET', 'POST'])
def index():

    # POST for uploading a pdf/txt or pasting/typing text and showing output
    if request.method == 'POST':
        # Get the inputs
        text_input = request.form.get('text_input')

        file = request.files.get('file')
        file_path = None

        # Check if correct files
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

        # Send the text/file to pipeline
        result = process_input(text_input, file_path)

        return render_template('results.html', result=result)

    # GET for getting pdf/txt or pasting/typing text
    if request.method == 'GET':
        return render_template('input.html')


# Send input to backend and get back output
def process_input(text_input, file_path):
    return {
        "summary": "Summary",
        "key_terms": ["Terms"],
        "questions": ["Questions"],
        "flashcards": [("Term", "Definition")]
    }


if __name__ == '__main__':
    app.run(debug=True)