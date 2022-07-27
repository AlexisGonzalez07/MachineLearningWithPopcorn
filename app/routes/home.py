import io
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Response,Blueprint, render_template

from home import df6820movies as df
from app.utils import _6820processing

matplotlib.use('Agg')

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
    # pg_df = df[df['rating']=='PG']
    # # r_df = df[df['rating']=='R']

    # fig, ax = plt.subplots(figsize = (6,4))
    # fig.patch.set_facecolor('#E8E5DA')

    # x = df.year
    # y1 = pg_df.budget
    # # y2 = r_df.budget

    # ax.bar(x, y1, color = "#304C89", width=0.5, label='PG')
    # # ax.bar(x+0.5, y2, color = "red", width=0.5, label='R')


    # plt.xticks(rotation = 10, size = 5)
    # plt.ylabel("Budget", size = 7)
    # plt.xlabel("Year")


    # return fig
    pg_df = df[df['rating']=='PG']
    
    total_budget = (pg_df.groupby(['year'])['budget'].sum())/100000
    years = pg_df['year'].unique()
    # pg_df['sum'] = values
    print(years)
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = years
    # xs = range(10) # x-axis coordinates
    # ys = [x for x in values] # y-axis coordinates
    axis.plot(xs,total_budget)
    # axis.plot(xs, ys)
    plt.ylabel("Budget * 100000", size = 7)
    plt.xlabel("Year")
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
    return render_template('by-actor.html')
    

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


