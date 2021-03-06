from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/main')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
