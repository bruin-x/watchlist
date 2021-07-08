from flask import Blueprint, render_template, session, request, redirect, url_for


bp_index = Blueprint('index', __name__, url_prefix='/')
bp_edit = Blueprint('edit', __name__, url_prefix='/edit')


from . import index
from . import login
from . import register
from . import edit


