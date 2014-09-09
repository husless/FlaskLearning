from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, TextAreaField, \
    PasswordField, validators
from flaskr.models import User

class LoginForm(Form):
    openid = TextField('openid', validators=[validators.Required()])
    remember_me = BooleanField('remember_me', default=False)

class EditForm(Form):
    nickname = TextField('nickname', validators=[validators.Required()])
    about_me = TextAreaField('about_me', validators=[validators.Length(min=0,max=140)])

    def __init__(self,original_nickname, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.original_nickname = original_nickname

        def validate(self):
            if not Form.validate(self):
                return False
            if self.nickname.data == self.original_nickname:
                return True
            user = User.query.filter_by(nickname=self.nickname.data).first()
            if user is not None:
                self.nickname.errors.append('This nickname is already in use. Please choose another one.')
                return False
            return True

class PostForm(Form):
    post = TextField('post', validators=[validators.Required()])
