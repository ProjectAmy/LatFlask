from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/students'
app.config['SECRET_KEY'] = "dfhbikaufhgayu"

db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column('Student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(20))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


@app.route('/')
def show_all():
    return render_template('show_all.html', students=Students.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Isi semua kolom dengan benar', 'error')
        else:
            student = Students(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash('Data berhasil ditambahkan')
            return redirect(url_for('show_all'))

    return render_template('new.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    student = Students.query.get_or_404(id)

    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Isi semua kolom dengan benar', 'error')
        else:
            student.name = request.form['name']
            student.city = request.form['city']
            student.addr = request.form['addr']
            student.pin = request.form['pin']
            db.session.commit()
            flash('data berhasil diupdate')
            return redirect(url_for('show_all'))

    return render_template('edit.html', student=student)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    student = Students.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('data telah berhasil dihapus')
    return redirect(url_for('show_all'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
