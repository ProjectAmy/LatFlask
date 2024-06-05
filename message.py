from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'jfdkhbgkjdfshdj'
app.config['UPLOAD_FOLDER'] = 'upload'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Batas ukuran file 16MB


@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            flash('pesan 1')
            flash('pesan 2')
            return redirect(url_for('index'))

    return render_template('login2.html', error=error)


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST', 'GET'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))

    return 'file uploaded successfully'


if __name__ == "__main__":
    app.run(debug=True)
