import sys, shutil

from flask import Flask, render_template, url_for, redirect, abort
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask.ext.assets import Environment

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

@app.route('/pages/<name>')
def page(name):
	""" render static pages """
	path = '{}/{}'.format(PAGE_DIR, name)
	page = flatpages.get_or_404(path)
	return render_template('page.html', page=page)

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

"""
@app.route('/pygments.css')
def pygments_css():
	return pygments_style_defs('manni'), 200, {'Content-Type': 'text/css'}
"""

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
        """shutil.rmtree('build/static/.webassets-cache')"""
    else:
        app.run(port=SERVER_PORT)