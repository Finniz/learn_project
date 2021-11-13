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
        try:
            db.session.commit()
            print(f'{usr} подписан на {shr}')
        except:
            print('Пользователь уже подписан на эту акцию') 
            db.session.rollback()   
             

def unsubscribe(username,sharename): 
    """
    Подписываем пользователя на ценные бумаги
    
    """
    usr = User.query.filter(User.username == username).first()
    shr_id = Share.query.filter(Share.stock_symbol == sharename).first()
    shr = db.session.query(Share).get(shr_id.id)
        
    if usr == None or shr == None:
        print('Ошибочные данные')
    else:
        shr.subscribers.remove(usr)
        try:
            db.session.commit()
            print(f'{usr} отписался от {shr}')
        except:
            print('Пользователь не подписан на эту акцию') 
            db.session.rollback()                
    
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        get_rises_5()
        get_falls_5()
        # unsubscribe('user1','M')
        