from flask import Response,Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

# homepage
@bp.route('/')
def index():
  return render_template('homepage.html')


# contact page
@bp.route('/contact')
def contact():
  return render_template('contact.html')