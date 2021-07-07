from wtforms.fields import simple
from wtforms import validators, Form, widgets



class Login(Form):
    username = simple.StringField(
        label='用户名',
        widget=widgets.TextInput(),
        validators=[validators.InputRequired(), validators.Length(max=20, min=1, message='长度超出！')],
        render_kw={'class': 'username', 'id': 'username'}
    )

    password = simple.PasswordField(
        label='密码',
        widget=widgets.PasswordInput(),
        validators=[validators.InputRequired(), validators.Length(max=16, min=1, message='长度超出！')],
        render_kw={'class': 'password', 'id': 'password'}
    )


class Register(Login):
    checkpassword = simple.PasswordField(
        label='确认密码',
        widget=widgets.PasswordInput(),
        validators=[validators.InputRequired(), validators.Length(max=16, min=1, message='长度超出！'), validators.EqualTo('password', message='密码必须一致！')],
        render_kw={'class': 'checkpassword', 'id': 'checkpassword'}
    )


class AddMovie(Form):
    title = simple.StringField(
        label='title',
        widget=widgets.TextInput(),
        validators=[validators.InputRequired(), validators.Length(max=100, min=1, message='长度超出！')],
        render_kw={'class': 'addmovie'}
    )

    year = simple.StringField(
        label='year',
        widget=widgets.TextInput(),
        render_kw={'class': 'addmovie'},
        validators=[validators.Length(min=4, max=4, message='输入的日期不规范！')]
    )

    



