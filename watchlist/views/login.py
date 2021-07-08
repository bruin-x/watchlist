from flask import request, render_template, flash, redirect, url_for
from flask import session
from wtforms import Form

from . import bp_index
from watchlist import models
from watchlist import forms


@bp_index.route('login/', methods=['GET', 'POST'])
def login():
    form = forms.Login()

    if request.method == 'POST':
        form = forms.Login(formdata=request.form)

        if form.validate():
            user = models.User.query.filter(models.User.name == form.username.data).first()
            
            if user:
                # 用户存在并且密码正确，跳转至index页面
                if user.check_password(form.password.data):
                    session['username'] = form.username.data
                    return redirect(url_for('index.index'))
                else:
                    flash('密码错误！')
                    return render_template('login.html', form=form)
    
            # 用户不存在跳转至注册页面
            return redirect(url_for('index.register'))
        # 输入格式错误重新加载
        return render_template('login.html', form=form)
    
    
    if request.method == 'GET':
        return render_template('login.html', form=form)