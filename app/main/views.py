from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, request, current_app
from . import main
from .. import db
from .forms import LoginForm, BlogForm, JournalForm
from ..models import Blog, Comment, Journal
from sqlalchemy import cast, DATE

@main.route('/', methods=['GET', 'POST'])
def index():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(body=form.body.data, title=form.title.data)
        try:
            db.session.add(blog)
        except:
            db.session.rollback()
            raise
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = Blog.query.order_by(Blog.timestamp.desc()).paginate(page, per_page=10, error_out=False)
    blogs = pagination.items
    return render_template('index.html', form=form, blogs=blogs, pagination=pagination)

@main.route('/blog/<int:id>', methods=['GET', 'POST'])
def blog(id):
    blog = Blog.query.get_or_404(id)
    return render_template('blog.html', id=id, blog=blog)

@main.route('/journal', methods=['GET', 'POST'])
def journalhome():
    if not session['logged_in']:
        return redirect(url_for('.index'))
    form = JournalForm()
    if form.validate_on_submit():
        journal = Journal(event=form.event.data,
                  costtime=form.costtime.data,
                  timestamp = datetime.utcnow(),
                  date = datetime.utcnow().date())
        try:
            db.session.add(journal)
        except:
            db.session.rollback()
            db.session.commit()
            raise
        return redirect(url_for('.journalhome'))
    dates = [date for (date, ) in db.session.query(Journal.date).distinct().order_by(Journal.date.desc())]
    journals = Journal.query
    #
    #****Pagination Function For Future Improve*****
    # page = request.args.get('page', 1, type=int)
    # pagination = paginate(query, page, per_page=10, error_out=False)
    # dates = pagination.items
    return render_template('journalhome.html', form=form, dates=dates, journals=journals)

@main.route('/journal/<date>', methods=['GET', 'POST'])
def journal(date):
    if not session['logged_in']:
        return redirect(url_for('.index'))
    journal = Journal.query.filter_by(date=date)
    form = JournalForm()
    if form.validate_on_submit():
        journal = Journal(event=form.event.data,
                  costtime=form.costtime.data)
        try:
            db.session.add(journal)
        except:
            db.session.rollback()
            raise
        return redirect(url_for('.journal', date=date))
    journals = Journal.query.filter_by(date=date)

    return render_template('journal.html', form=form, date=date, journals=journals)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == current_app.config['ADMIN_USERNAME'] and \
           form.password.data == current_app.config['ADMIN_PASSWORD']:
           session['logged_in'] = True
           flash('You were logged in')
           return redirect(url_for('main.index'))
        flash('Invalid username or password.')

    return render_template('login.html', form=form)

@main.route('/logout')
def logout():
    session['logged_in'] = False
    flash('You were logged out')
    return redirect(url_for('main.index'))
