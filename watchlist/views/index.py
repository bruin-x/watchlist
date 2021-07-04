from flask import render_template, request, redirect, url_for, flash

from . import bp_index
from watchlist import models
from watchlist import forms


name = 'Xiong Renyi'

movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]



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

