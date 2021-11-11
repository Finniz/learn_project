from flask import Blueprint, render_template
from webapp.model import Share
from sqlalchemy import desc
from exchange_rates import dollar_value, euro_value, bitcoin_value
import indeces

blueprint = Blueprint('main_page', __name__)



@blueprint.route("/")
def index():
    title = "Инвестиции"
    fall = Share.query.order_by('todays_range').limit(5).all()
    height = Share.query.order_by(desc('todays_range')).limit(5).all()
    dollar = ('$ ' + str(dollar_value()))
    euro = ('€ ' + str(euro_value()))
    bitcoin = ('₿ ' + str(bitcoin_value()))
    idx = indeces.idx

    return render_template('main_page/index.html', page_title=title, height=height, fall=fall, 
    dollar=dollar, euro=euro, bitcoin=bitcoin, idx=idx
    )
