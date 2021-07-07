from flask import request, render_template, flash, redirect, url_for
from wtforms import Form

from . import bp_index
from watchlist import models
from watchlist import forms


@bp_index.route('login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = forms.Login(formdata=request.form)

        if form.validate():
            user = models.User.query.filter(models.User.name == form.username._value()).first()
            
            if user:
                if user.check_password(form.password._value()):
                    return '登录成功！'
                else:
                    return '登录失败！'
            
            return redirect(url_for('index.register'))

        else:
            return render_template('login.html', form=form)
    
    
    if request.method == 'GET':
        form = forms.Login()
        return render_template('login.html', form=form)