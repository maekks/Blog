from . import db
from flask import current_app, request, url_for
from datetime import datetime

class Permission:
    WRITE_POST = 0X01
    COMMENT = 0X02
    ADMINISTER = 0X80

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='blogs', lazy='dynamic')

class Journal(db.Model):
    __tablename__ = 'journals'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.Text)
    costtime = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True)
    date = db.Column(db.Date, index=True)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    disabled = db.Column(db.Boolean)
    post_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
