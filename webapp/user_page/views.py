from flask import Blueprint, render_template

blueprint = Blueprint('user_page', __name__, url_prefix='/user')

@blueprint.route("/")
def user():
    title = "Личный кабинет"
    return render_template('user_page/user.html', page_title=title)

    
