from mongoengine import *
from werkzeug.security import generate_password_hash,check_password_hash #加密驗證
from flask_login import UserMixin


#user models
class User(UserMixin,Document):
    username = StringField(required=True)
    password_hash = StringField(required=True)
    role = StringField(required=True)
    meta = {"collection" : "users"}
    
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
#EDA_img EmbeddedDocument
class EDA_img(EmbeddedDocument):
     name = StringField()
     file = FileField()
#album models
class Album(Document):
    meta = {"collection" : "albums"}
    title = StringField(required = True,min_length=1)
    text = StringField()
    show = StringField()
    index = IntField(default=0)
    album_imgs = EmbeddedDocumentListField(EDA_img)
   
class New(Document):
    meta = {"collection" : "news"}
    title = StringField(required = True,min_length=1)
    text = StringField()
    show = StringField()
    tag = StringField()
    add_date = DateField()
    new_imgs = EmbeddedDocumentListField(EDA_img)


class Fs_chunks(Document):
    meta = {"collection" : "fs.chunks"}
    files_id = StringField()
    n = IntField()
    data = BinaryField()

class Fs_files(Document):
    meta = {"collection" : "fs.files"}
    filename = StringField()
    chunkSize = IntField()
    length = IntField()
    uploadDate = DateField()