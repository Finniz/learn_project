from webapp.model import Share, db, subs
from webapp.user.models import User
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
        
        
def get_subscribe(username,sharename): 
    """
    Подписываем пользователя на ценные бумаги
    
    """
    usr = User.query.filter(User.username == username).first()
    shr = Share.query.filter(Share.stock_symbol == sharename).first()
    if usr == None or shr == None:
        print('Ошибочные данные')
    else:
        shr.subscribers.append(usr)
        db.session.commit()
        print(f'{usr} подписан на {shr}')     
    
      
    
          

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # get_rises_5()
        # get_falls_5()
        # get_subscribe('user1', 'F')
        usr = User.query.all()
        for user in usr:
            print(f'{user.username} подписан на', *user.subscriptions, sep='\n')