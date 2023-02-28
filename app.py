from flask import Flask
from flask import render_template
from flask import redirect
from flask import  request

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
    return render_template('about.html',index=False)

@app.route('/history', methods=['GET', 'POST'])
def history():  # put application's code here
    return render_template('history.html',index=False)

@app.route('/blog', methods=['GET', 'POST'])
def blog():  # put application's code here
    return render_template('bulletin.html',index=False)

@app.route('/organizational_chart', methods=['GET', 'POST'])
def organizational_chart():  # put application's code here
    return render_template('organizational_chart.html',index=False)



if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.run(debug=True)