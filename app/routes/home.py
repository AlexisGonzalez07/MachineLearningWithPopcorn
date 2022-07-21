from flask import Blueprint, render_template
bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def index():
  return render_template('homepage.html')


@bp.route('/graph')
def chart():
    data = [
        ('name1',2003),
        ('name2',2004),
        ('name3',2005),
        ('name4',2006),
        ('name5',2007),
        ('name6',2008)
    ]

    labels = [row[0] for row in data]  
    values = [row[1] for row in data]

    return render_template('graph.html',
                          labels=labels,
                          values=values)


