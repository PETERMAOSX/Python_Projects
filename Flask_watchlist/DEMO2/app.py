from datetime import timedelta
import os
import sys
import click

from flask import render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


WIN = sys.platform.startswith('win')

if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)

#模型类声明要继承db.Model 每一类字段要实例化db.Column
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

@app.cli.command() #注册为命令
@click.option('--drop',is_flag=True,help='Create after drop.')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("Initialized database.")
@app.cli.command()
def forge():
    db.create_all()
    name = 'Petermaosx'
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
    user = User(name=name)
    db.session.add(user)

    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('Done.')
@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html',movies=movies)

# @app.errorhandler(404)  # 传入要处理的错误代码
# def page_not_found(e):  # 接受异常对象作为参数
#     user = User.query.first()
#     return render_template('404.html', user=user), 404  # 返回模板和状态码

@app.context_processor   #全局变量
def inject_user():
    user = User.query.first()
    return dict(user=user)

@app.errorhandler(404)
def page_not_find(e):
    return render_template('404.html'),404



# @app.route('/')
# def hello():
#     return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

# @app.route("/home")
# def hello1():
#     return "主页"

# @app.route('/user/<name>')
# def user_page(name):
#     return 'User: %s' % escape(name)