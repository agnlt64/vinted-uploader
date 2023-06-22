from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import secrets

db = SQLAlchemy()

class VintedItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(5), nullable=False)
    quality = db.Column(db.String(2), nullable=False)
    code = db.Column(db.String(10), unique=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(40)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items/upload', methods=['POST'])
def uploae_item():
    if request.method == 'POST':
        type = request.form.get('type')
        brand = request.form.get('brand')
        color = request.form.get('color')
        quality = request.form.get('quality')
        if type == "" or brand == "" or color == "" or quality == "":
            flash('Tous les champs sont requis!', category='error')
            return render_template('index.html')
        else:
            new_item = VintedItem(type=type, brand=brand, size='none', color=color, quality=quality)
            db.session.add(new_item)
            db.session.commit()
        flash('Item ajouté!', category='success')
    return render_template('index.html')

@app.route('/items/all')
def all_items():
    return render_template('all_items.html', items=VintedItem.query.all())

if __name__ == '__main__':
    app.run(debug=True, port=8080)
