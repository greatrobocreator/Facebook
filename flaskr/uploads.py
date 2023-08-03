import os
import random

from flask import (
    Blueprint, flash, g, redirect, url_for, request, current_app,
    send_from_directory
)

from werkzeug.exceptions import abort

bp = Blueprint('uploads', __name__)


def is_image(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}


@bp.route('/upload_image', methods=('POST',))
def upload_image():
    # return 'ok'
    print('Something!')
    if 'file' not in request.files:
        flash('File not uploaded')
        return redirect('index')
    print('Uploading file')
    file = request.files['file']
    if file is None or file.filename == '' or not is_image(
            file.filename):
        flash('Wrong file')
        return redirect(request.url)

    filename = hex(random.getrandbits(128)).lstrip('0x') + '.' + \
               file.filename.rsplit('.', 1)[1].lower()
    # secure_filename(file.filename)
    print('Saving ', filename)
    path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(path)

    # redirect(url_for('index'))

    return url_for('uploads.uploads', filename=filename)


@bp.route('/uploads/<filename>')
def uploads(filename):
    if not filename:
        abort(404)

    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
