from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('user', __name__)


@bp.route('/')
@login_required
def index():
    return redirect(url_for('user.user', id=str(g.user['id'])))


@bp.route('/id<int:id>')
def user(id):
    db = get_db()
    user = db.execute(
        'SELECT id, username, about, avatar'
        ' FROM user u'
        ' WHERE u.id = ?',
        (id,)
    ).fetchone()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE u.id = ?'
        ' ORDER BY created DESC',
        (id,)
    ).fetchall()
    return render_template('user/index.html', user=user, posts=posts)
    # return str(user['username'])
