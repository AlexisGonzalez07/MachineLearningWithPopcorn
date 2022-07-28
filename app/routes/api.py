from flask import Blueprint, request, jsonify
import sys
from app.utils._6820processing import main6820
from home import df6820movies as df




bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/actor/<actor>', methods=['POST'])
def search(actor):
    df1 = main6820(df)
    # filter df even for partial match
    actor_search = df1['star'].str.contains(actor, na=False, case=False)
    actor_res = df1[actor_search]
    # count total rows
    total_movies = actor_res.shape[0] 
    # list genres
    list_genre = actor_res['genre'].unique()
    # count total movies by genre
    genra_count = actor_res.groupby(['genre']).size()

    labels = [x for x in list_genre]
    values = [x for x in genra_count]
    colors = [
        "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
        "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
        "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
    res={"values":values, "labels":labels, "colors":colors, "total":total_movies}
    return res 