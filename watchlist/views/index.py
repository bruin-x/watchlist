from flask import render_template, request, redirect, url_for, flash, session

from . import bp_index
from watchlist import models
from watchlist import forms


@bp_index.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # 添加单个电影条目
        form = forms.AddMovie(formdata=request.form)
    
        if form.validate():
            movie = models.Movie(title=form.title.data, year=form.year.data, user_id=1)
            models.db.session.add(movie)
            models.db.session.commit()

            return redirect(url_for('index.index'))

        return render_template('index.html', form=form)
       
    
    elif request.method == 'GET':
        form = forms.AddMovie()
        movies = models.Movie.query.filter(models.Movie.user_id == 1).all()
        user = models.User.query.filter(models.User.id == 1).first()

        return render_template('index.html', form=form, movies=movies, name=user.name)

    

@bp_index.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@bp_index.before_request
def is_login():
    if session.get('username'):
        return
    
    if request.path == '/login/':
        return
    
    if request.path == '/register/':
        return
    
    return redirect(url_for('index.login'))
