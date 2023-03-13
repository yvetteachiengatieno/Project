from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle= 'Server main page')

@app.route('/enrollment')
def enrollment():
    return render_template('enrollment.html', pageTitle='List of enrollment')

if __name__ == '__main__':
    app.run(debug=False)