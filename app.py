from flask import Flask
from flask import render_template

import s3_functions
from s3_functions import list_files, upload_file, list_image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    return render_template('index.html',index=False)

@app.route('/news', methods=['GET', 'POST'])
def news():  # put application's code here
    return render_template('news.html',index=False)

@app.route('/album', methods=['GET', 'POST'])
def album():  # put application's code here
    return render_template('album.html',index=False)

@app.route('/about', methods=['GET', 'POST'])
def about():  # put application's code here
    about_pic = s3_functions.list_image('yaoweb')
    return render_template('about.html',about_pic=about_pic[3],index=False)

@app.route('/history', methods=['GET', 'POST'])
def history():
    history_pic = s3_functions.list_image('yaoweb')
    return render_template('history.html',history_pic=history_pic[4],index=False)

@app.route('/blog', methods=['GET', 'POST'])
def blog():  # put apfirst_organizational_chartplication's code here
    return render_template('bulletin.html',index=False)

@app.route('/four_organizational_chart', methods=['GET', 'POST'])
def four_organizational_chart():  # put application's code here
    return render_template('four_organizational_chart.html', index=False)


@app.route('/first_organizational_chart', methods=['GET', 'POST'])
def first_organizational_chart():  # put application's code here
    return render_template('first_organizational_chart.html', index=False)

@app.route('/second_organizational_chart', methods=['GET', 'POST'])
def second_organizational_chart():  # put application's code here
    return render_template('second_organizational_chart.html', index=False)

@app.route('/thired_organizational_chart', methods=['GET', 'POST'])
def thired_organizational_chart():  # put application's code here
    return render_template('thired_organizational_chart.html', index=False)

@app.route('/five_organizational_chart', methods=['GET', 'POST'])
def five_organizational_chart():  # put application's code here
    return render_template('five_organizational_chart.html', index=False)


if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)