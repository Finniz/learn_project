from flask import Blueprint, render_template
from webapp.user_page.models import Share

blueprint = Blueprint('user_page', __name__, url_prefix='/user')

@blueprint.route("/")
def user():
    title = "Личный кабинет"
    

    return render_template('user_page/user.html', page_title=title)
    
