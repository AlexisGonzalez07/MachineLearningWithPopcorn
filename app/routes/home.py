import io
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Response,Blueprint, render_template

# import datasets
from home import df6820movies as df
from home import df5000movies
from home import df5000credits
# import util functions
from app.utils._6820processing import main6820

matplotlib.use('Agg')

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def index():
  return render_template('homepage.html')


@bp.route('/plot-pg-score.png')
def plot_pg_png():
    fig = create_score_pg_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_score_pg_figure():
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


    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    df1 = main6820(df)
    pg_df = df1[df1['for_kids']==1]    
    print(pg_df)
    xs = df1['year'].unique()

    # budget
    pg_total_budget = (pg_df.groupby(['year'])['budget'].sum())/1000000
    axis.plot(xs,pg_total_budget,label='Budget')

    # gross
    pg_total_gross = (pg_df.groupby(['year'])['gross'].sum())/1000000
    axis.plot(xs,pg_total_gross,label='Profit')
 
    axis.set_title('Kids Rating Budget/Profit')
    axis.set_ylabel("Amount in Mil", size = 7)
    axis.set_xlabel("Year")
    axis.legend()

    return fig

@bp.route('/plot-r-score.png')
def plot_r_png():
    fig = create_score_r_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_score_r_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    df1 = main6820(df)
    r_df = df1[df1['for_kids']==0]    
    xs = df1['year'].unique()

    # budget
    r_total_budget = (r_df.groupby(['year'])['budget'].sum())/1000000
    axis.plot(xs,r_total_budget,label='Budget')

    # profit 
    r_total_gross = (r_df.groupby(['year'])['gross'].sum())/1000000
    axis.plot(xs,r_total_gross,label='Profit')
 
    axis.set_title('Adult Rating Budget/Profit')
    axis.set_ylabel("Amount in Mil", size = 7)
    axis.set_xlabel("Year")
    axis.legend()

    return fig

@bp.route('/rating')
def rating():
    return render_template('by-rating.html')

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


