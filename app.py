from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Define the folder to store uploaded videos
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # Limit upload size to 100 MB

# Ensure the upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return 'No video part'
    file = request.files['video']
    if file.filename == '':
        return 'No selected file'
    if file:
        # Save the uploaded video file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return f'Video successfully uploaded: {file.filename}'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

