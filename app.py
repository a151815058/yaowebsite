from flask import Flask
from flask import render_template
from flask import  request

app = Flask(__name__)

@app.route('/news')
@app.route('/')
def start():  # put application's code here
    return render_template('news.html')


@app.route('/album')
def album():  # put application's code here
    return render_template('album.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/history')
def history():  # put application's code here
    return render_template('history.html')

if __name__ == '__main__':
    app.run()