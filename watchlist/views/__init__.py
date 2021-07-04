from flask import Blueprint, render_template


bp_index = Blueprint('index', __name__, url_prefix='/')


from . import index