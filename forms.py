from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,PasswordField,BooleanField,SubmitField,SelectField,IntegerField,MultipleFileField,TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    class Meta:
        csrf =False
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    submit = SubmitField("登入")

class AddAlbumForm(FlaskForm):
    class Mata:
        csrf=False
    title = StringField("相簿名稱",validators=[DataRequired()])
    text = TextAreaField("說明")
    show = SelectField("是否顯示",coerce=int,choices=[(1 ,"顯示"),(2,"不顯示")])
    index = IntegerField("排序(數值越大越高)",validators=[DataRequired()])
    album_imgs = FileField(label='請上傳圖片',validators=[FileAllowed(['jpg','png','jpeg','GIF'],message="僅支援JPG.JPEG.PNG.GIF格式")])
    submit = SubmitField("確認")
    delete = SubmitField("刪除相簿")