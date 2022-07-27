from flask import Blueprint, request, jsonify
import sys
from app.utils._6820processing import main6820
from home import df6820movies as df




bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/actor/<actor>', methods=['POST'])
def search(actor):
    df1 = main6820(df)
    actor_res = df1[df1['star']==actor]
    genra_count = actor_res.groupby(['genre']).size()
    print(genra_count)
    labels = ['action','advent','anima','bio','comedy','drama']
    values = [x for x in genra_count]
    colors = [
        "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
        "#ABCDEF", "#DDDDDD"]
    res={"values":values, "labels":labels, "colors":colors}
    # print(genra_count) 
    return res 