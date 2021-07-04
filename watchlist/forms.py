from wtforms.fields import simple
from wtforms import validators, Form, widgets



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

    



