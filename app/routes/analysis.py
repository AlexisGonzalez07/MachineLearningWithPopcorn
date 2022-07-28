import io
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

bp = Blueprint('analytics', __name__, url_prefix='/analytics')


@bp.route('/plot-pg-score.png')
def plot_pg_png():
    fig = create_score_pg_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_score_pg_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    df1 = main6820(df)
    pg_df = df1[df1['for_kids']==1]    
    # print(pg_df)
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
    return render_template('by-year.html')


