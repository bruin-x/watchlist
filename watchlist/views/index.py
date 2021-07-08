from flask import render_template, request, redirect, url_for, flash, session, g

from . import bp_index
from watchlist import models
from watchlist import forms


@bp_index.route('')
def index():
    # 展示已登录用户待看电影
    form = forms.Movie()

    username = session.get('username')
    user_id = models.User.query.filter(models.User.name == username).first().id
    movies = models.Movie.query.filter(models.Movie.user_id == user_id).all()

    return render_template('index.html', form=form, movies=movies, name=username)

    

@bp_index.before_request
def is_login():
    if session.get('username'):
        return
    
    if request.path == '/login/':
        return
    
    if request.path == '/register/':
        return
    
    return redirect(url_for('index.login'))


@bp_index.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


