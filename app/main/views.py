from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, request, current_app
from . import main
from .. import db
from ..models import Blog, Comment, Journal

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
