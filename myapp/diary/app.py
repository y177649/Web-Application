from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Entry {self.title}>'

@app.route('/')
def index():
    entries = Entry.query.order_by(Entry.date.desc()).all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    title = request.form['title']
    date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    content = request.form['content']
    tags = request.form['tags']
    
    new_entry = Entry(title=title, date=date, content=content, tags=tags)
    db.session.add(new_entry)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
5