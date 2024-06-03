from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'hello word'


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
