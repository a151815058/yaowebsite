from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_ckeditor import CKEditorField
from wtforms import StringField,PasswordField,BooleanField,SubmitField,SelectField,IntegerField,MultipleFileField,TextAreaField,DateField
from wtforms.validators import DataRequired
import datetime

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
    text = CKEditorField("說明")
    show = SelectField("是否顯示",coerce=str,choices=[("顯示" ,"顯示"),("不顯示","不顯示")])
    index = IntegerField("排序(數值越大越高)",validators=[DataRequired()])
    album_imgs = FileField(label='請上傳圖片',validators=[FileAllowed(['jpg','png','jpeg','GIF'],message="僅支援JPG.JPEG.PNG.GIF格式")])
    submit = SubmitField("確認")
    delete = SubmitField("刪除相簿")


class AddNewForm(FlaskForm):
    class Mata:
        csrf=False
    title = StringField("標題",validators=[DataRequired()])
    text = CKEditorField("內容")
    show = SelectField("是否顯示",coerce=str,choices=[("顯示" ,"顯示"),("不顯示","不顯示")])
    tag = SelectField("分類",coerce=str,choices=[("活動公告" ,"活動公告"),("會議公告","會議公告"),("系統公告","系統公告")])
    add_date = DateField("公告日期",id='add_date',validators=[DataRequired()],default=datetime.date.today)
    new_imgs = FileField(label='請上傳圖片',validators=[FileAllowed(['jpg','png','jpeg','GIF'],message="僅支援JPG.JPEG.PNG.GIF格式")])
    submit = SubmitField("確認")
    delete = SubmitField("刪除最新消息")