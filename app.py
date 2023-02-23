from flask import Flask
from flask import render_template
from flask import  request

app = Flask(__name__)


@app.route('/')
def start():  # put application's code here
    return render_template('index.html')

@app.route('/album')
def album():  # put application's code here
    return render_template('album.html')


if __name__ == '__main__':
    app.run()