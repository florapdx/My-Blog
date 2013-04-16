import sys, shutil

from flask import Flask, render_template, url_for, redirect, abort
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from flask.ext.assets import Environment
#from pygments import highlight
#from pygments.formatters import HtmlFormatter
from datetime import date, datetime


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'
PAGE_DIR = 'pages'
FLATPAGES_EXTENSION = '.md'
SITE_NAME = 'Diary of a Future Dev'
SERVER_PORT = 8000

app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
assets = Environment(app)
assets.url_expire = False

@app.route('/')
def index():
	""" Show a list of most recent posts on index page """
	posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
	return render_template('index.html', posts=posts)

@app.route('/tutorials/')
def tutorials():
	""" Show a list of most recent posts on index page """
	posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
	return render_template('tutorials.html', posts=posts)

@app.route('/community/')
def community():
	""" Show a list of most recent posts on index page """
	posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
	return render_template('community.html', posts=posts)

@app.route('/events/')
def events():
	""" Show a list of most recent posts on index page """
	posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
	return render_template('events.html', posts=posts)

@app.route('/resources/')
def resources():
	""" Show a list of most recent posts on index page """
	return render_template('resources.html')

@app.route('/about/')
def about():
	""" Show a list of most recent posts on index page """
	return render_template('about.html')

@app.route('/portfolio/')
def portfolio():
	""" Show a list of most recent posts on index page """
	return render_template('portfolio.html')


@app.route('/pages/<name>')
def page(name):
	""" render static pages """
	path = '{}/{}'.format(PAGE_DIR, name)
	page = flatpages.get_or_404(path)
	return render_template('page.html', page=page, pages=pages)

@app.route('/posts/<name>')
def post(name):
	""" render posts """
	path = '{}/{}'.format(POST_DIR, name)
	post = flatpages.get_or_404(path)
	return render_template('post.html', post=post)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/events/<name>')
def event(name):
	""" render events """
	path = '{}/{}'.format(EVENT_DIR, name)
	event = flatpages.get_or_404(path)
	return render_template('event.html', event=event)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('manni'), 200, {'Content-Type': 'text/css'}

@app.route('/404.html')
def error404():
	return render_template('404.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
        """shutil.rmtree('build/static/.webassets-cache')"""
    else:
        app.run(port=SERVER_PORT)