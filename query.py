from webapp.model import Share
from webapp.user.models import User, subs
from webapp import create_app


def get_rises_5():
    """
    Получаем из БД 5 наиболее выросших/наименее упавших в цене акций 
    
    """  
    shares = Share.query.order_by(Share.todays_range.desc()).limit(5)
    for share in shares:
        print(share)


def get_falls_5():
    """
    Получаем из БД 5 наиболее упавших/наименее выросших в цене акций 
    
    """  
    shares = Share.query.order_by(Share.todays_range.asc()).limit(5)
    for share in shares:
        print(share)

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        get_rises_5()
        get_falls_5()