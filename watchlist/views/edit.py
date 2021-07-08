from flask import render_template, request, redirect, url_for, flash, session, g

from . import bp_edit
from watchlist import models
from watchlist import forms


@bp_edit.route('/')
def edit():
    form = forms.Movie()
    
    username = session.get('username')
    user_id = models.User.query.filter(models.User.name == username).first().id
    movies = models.Movie.query.filter(models.Movie.user_id == user_id).all()

    return render_template('edit.html', form=form, movies=movies, name=username)


@bp_edit.route('add/', methods=['POST'])
def add():
    # 添加电影条目
    form = forms.Movie(formdata=request.form)

    if form.validate():
        username = session.get('username')
        user_id = models.User.query.filter(models.User.name == username).first().id
        movie = models.Movie(title=form.title.data, year=form.year.data, user_id=user_id)
        try:
            models.db.session.add(movie)
            models.db.session.commit()
        except Exception:
            return '提交失败！'
    else:
        flash('输入有误！')

    return redirect(url_for('edit.edit'))
    
        
    


@bp_edit.route('dele/<string:movie_id>', methods=['GET', 'POST'])
def dele(movie_id=None):
    movie = models.Movie.query.filter(models.Movie.id == movie_id).first()
    models.db.session.delete(movie)
    models.db.session.commit()
    flash('删除成功！')

    return redirect(url_for('edit.edit'))



@bp_edit.route('change/', methods=['POST'])
def change():
    pass


@bp_edit.before_request
def is_login():
    if session.get('username'):
        return
    
    if request.path == '/login/':
        return
    
    if request.path == '/register/':
        return
    
    return redirect(url_for('index.login'))