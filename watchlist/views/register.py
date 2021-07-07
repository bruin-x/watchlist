from flask import request, render_template, flash, redirect, url_for, session
from wtforms import Form

from watchlist import db
from . import bp_index
from watchlist import models
from watchlist import forms


@bp_index.route('register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = forms.Register(formdata=request.form)

        if form.validate():
            user = models.User(name=form.username._value(), password=form.password._value())
            print(form.username._value(),form.password._value() )
            db.session.add(user)
            db.session.commit()
        
            flash('注册成功！跳转至index')
            
            return redirect(url_for('index.index'))
        else:
            return render_template('register.html', form=form)

    return render_template('register.html', form=forms.Register())
            


