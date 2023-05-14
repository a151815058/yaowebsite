import sys
sys.path.append("/volume1/web/yaowebsite/")
from flask import Flask,redirect,url_for,render_template,request
from flask_login import LoginManager,login_user,logout_user,current_user,login_required
import mongoengine as me
import s3_functions
from s3_functions import list_files, upload_file, list_image
from models import User,Album,Album_img,Fs_chunks,Fs_files
from forms import LoginForm,AddAlbumForm
import base64

app = Flask(__name__)

me.connect('yaowebsiteDB',host='Your_DB_host', port=27017)
app.config['SECRET_KEY'] = 'yaoweb123'

loginMag = LoginManager()
loginMag.init_app(app)
loginMag.login_view = 'login'

@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    return render_template('index.html',index=False)

@app.route('/news', methods=['GET', 'POST'])
def news():  # put application's code here
    return render_template('news.html',index=False)

@app.route('/album', methods=['GET'])
def album():  # put application's code here
    albums = Album.objects(show=1).order_by("-index")
    return render_template('album.html',albums = albums,base64=base64)

@app.route('/album/<id>', methods=['GET'])
def album_id(id):  # put application's code here
    album = Album.objects.get(id=id)
    return render_template('album_id.html',index=False,album = album,base64=base64)


@app.route('/about', methods=['GET', 'POST'])
def about():  # put application's code here
    about_pic = s3_functions.list_image('yaoweb')
    return render_template('about.html',about_pic=about_pic[3],index=False)
    #return render_template('about.html',index=False)
@app.route('/history', methods=['GET', 'POST'])
def history():
    history_pic = s3_functions.list_image('yaoweb')
    return render_template('history.html',history_pic=history_pic[4],index=False)
    #return render_template('history.html',index=False)
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

###############後台相關區###########################

#使用者資料、驗證
@loginMag.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()


@app.route('/yaoadmin/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('yaoadmin_index'))
    form = LoginForm()
    if form.validate_on_submit():
        try:
            u = User.objects.get(username = form.username.data)
            if u.check_password(form.password.data):
                login_user(u)
                next_page = request.args.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect(url_for('yaoadmin_index'))
            else:
                #print("帳號或密碼錯誤")
                return redirect(url_for("login"))
        except me.DoesNotExist:
            #print("帳號或密碼錯誤")
            return redirect(url_for("login"))
        #return redirect('/')
    return render_template('login.html',form=form)


@app.route('/yaoadmin/index')
@login_required
def yaoadmin_index():
    return render_template('yaoadmin_index.html')


#活動花絮
@app.route('/yaoadmin/album')
@login_required
def yaoadmin_album():
    albums = Album.objects.all()

    return render_template('yaoadmin_album.html',albums=albums)


#活動花絮修改
@app.route('/yaoadmin/album/<album_id>',methods=['GET', 'POST'])
@login_required
def yaoadmin_album_id(album_id):
    form = AddAlbumForm()
    try:
        album = Album.objects.get(id=album_id)
    except:
        return "沒有找到這個ID"
    if request.method == "GET":
        form.title.data = album.title
        form.show.data = album.show
        form.index.data = album.index
        form.text.data = album.text
        return render_template('yaoadmin_album_id.html',form = form,album=album,base64=base64)

    if form.validate_on_submit():
        if form.submit.data:#確認鍵
            album.title = form.title.data
            album.show = form.show.data
            album.index = form.index.data
            album.text = form.text.data
            for filename in request.files.getlist("album_imgs"):
                if filename.filename == "":#如果無上傳 不加入
                    break
                i = Album_img(name=filename.filename)
                i.file.put(filename,filename=filename.filename)
                album.album_imgs.append(i)
            album.save()
            return redirect(url_for('yaoadmin_album'))
        if form.delete.data:#刪除鍵
            for img in album.album_imgs:
                Fs_chunks.objects(files_id = img.file._id).delete()
                Fs_files.objects(id=img.file._id).delete()
            album.delete()
            return redirect(url_for('yaoadmin_album'))
    
#刪除相簿圖片
@app.route('/api/del_album_img/<album_id>/<album_img_file>',methods=['GET'])
def api_del_album_img(album_id,album_img_file):
    album = Album.objects(id=album_id).first()
    
    for item in album.album_imgs:
        if str(item.file._id) == album_img_file:
            #print("有成功找到這個東西喔~~")
            album.album_imgs.remove(item)
            Fs_chunks.objects(files_id = item.file._id).delete()
            Fs_files.objects(id=item.file._id).delete()
            break
    album.save()
    return redirect(url_for('yaoadmin_album_id',album_id=album_id))

#新增活動花絮相簿
@app.route('/yaoadmin/add_album',methods=['GET', 'POST'])
@login_required
def yaoadmin_add_album():
    form = AddAlbumForm()
    if form.validate_on_submit():
        album_file = Album(title=form.title.data,show=form.show.data,index = form.index.data,text=form.text.data)
        #imgs = []
        for filename in request.files.getlist("album_imgs"):
            if filename.filename == "":#如果無上傳 不加入
                break
            i = Album_img(name=filename.filename)
            i.file.put(filename)
            album_file.album_imgs.append(i)
        #album_file.album_imgs = imgs
        album_file.save()
        return redirect(url_for("yaoadmin_album"))

    return render_template('yaoadmin_add_album.html',form=form)

#添加使用者帳號 勿刪
# @app.route('/test/add_data')
# def add_data():
#     u = User(username = 'test1',role='user')
#     u.set_password("test1")
#     u.save()
#     return '添加成功'

#登出
@app.route('/logout')  
def logout():  
    logout_user()  
    return redirect(url_for("login"))
###################################################


if __name__ == '__main__':
    #app.run(host='127.0.0.1',port=8080,debug=True)
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080,threads=10)