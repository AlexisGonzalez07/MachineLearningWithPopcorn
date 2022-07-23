from flask import Response,Blueprint, render_template
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
bp = Blueprint('home', __name__, url_prefix='/')





@bp.route('/')
def index():
  return render_template('homepage.html')


@bp.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
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
    print(values)
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(10) # x-axis coordinates
    ys = [random.randint(1, 50) for x in values] # y-axis coordinates
    axis.plot(values, ys)
    return fig



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


