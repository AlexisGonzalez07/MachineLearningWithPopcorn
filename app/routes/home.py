from flask import Blueprint, render_template
bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def index():
  return render_template('homepage.html')


@bp.route('/rating')
def rating():
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

    return render_template('by-rating.html',
                          labels=labels,
                          values=values)

@bp.route('/actor')
def actor():
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

    return render_template('by-actor.html',
                          labels=labels,
                          values=values)

@bp.route('/year')
def year():
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

    return render_template('by-year.html',
                          labels=labels,
                          values=values)


