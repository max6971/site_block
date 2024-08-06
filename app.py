from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Главная страница
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# Страница "О нас"
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)