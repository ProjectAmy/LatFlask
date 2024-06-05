from flask import Flask, redirect, url_for, render_template, request, make_response, session

app = Flask(__name__)
app.secret_key = 'jfdkhbgkjdfshdj'



@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
            "<b><a href = '/logout'>click here to log out</a></b>"

    return "You are not logged in <br><a href = '/login'></b>" + \
            "click here to log in</b></a>"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return '''
            <form action = "" method = "post">
            <p><input type = text name = username/></p>
            <p<<input type = submit value = Login/></p>
            </form>
            '''


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/kue')
def kue():
    return render_template('kue.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setccookie():
    if request.method == 'POST':
        user = request.form['nm']
    else:
        user = request.args.get('nm')

    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)

    return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>Selamat datang '+name+'</h1>'



@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/hasil', methods=['POST', 'GET'])
def hasil():
    if request.method == 'POST':
        hasil = request.form
        return render_template('hasil.html', hasil=hasil)
    else:
        hasil = request.args
        return render_template('hasil.html', hasil=hasil)


@app.route('/result')
def result():
    hasil = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=hasil)


@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello.html', marks=score)


@app.route('/nama')
def nama():
    return 'nama saya adalah sidra'


@app.route('/nama/<string:name>')
def getnama(name):
    return 'nama saya adalah : {}'.format(name)


@app.route('/admin')
def hello_admin():
    return 'hello admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hi, % as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True)
