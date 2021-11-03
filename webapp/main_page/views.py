from flask import Blueprint, render_template
from webapp.model import Share
from sqlalchemy import desc

blueprint = Blueprint('main_page', __name__)


@blueprint.route("/")
def index():
    title = "Инвестиции"
    fall = Share.query.order_by('todays_range').limit(5).all()
    height = Share.query.order_by(desc('todays_range')).limit(5).all()
    return render_template('main_page/index.html', page_title=title, height=height, fall=fall)
