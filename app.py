# -*- coding:utf-8 -*-

"""
# Time: 2024/9/3 10:51
# Author: Zhu, Dongshu
# File: app.py.py
# Version: python 3.9.13
# Description: 
"""
import logging
import os

import click
from flask import Flask, url_for, render_template
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.path.join(app.root_path, 'data.db')
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


@app.cli.command()
def forge():
    db.create_all()
    name = 'Zhu, Dongshu'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
    ]

    user = User(name=name)
    db.session.add(user)

    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')

@app.route('/')
def hello():
    name = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', name=name.name, movies=movies)


@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'


@app.route('/test')
def test():
    print(url_for('hello'))
    print(url_for('user_page', name='Zhu, Dongshu'))
    print(url_for('user_page', name='Black Monkey'))
    print(url_for('test'))
    print(url_for('test', num=2))
    return "Test page"


if __name__ == '__main__':
    app.run(debug=True)
