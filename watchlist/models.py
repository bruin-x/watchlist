from watchlist import db
from werkzeug.security import generate_password_hash, check_password_hash


user_movie = db.Table(
    'user_movie',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True)
)


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字
    _password = db.Column(db.String(16))

    movie = db.relationship('Movie', backref='user', secondary=user_movie)      #多对多关系

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, user_pw):
        return check_password_hash(self._password, user_pw)



class Movie(db.Model):  # 表名将会是 movie
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)