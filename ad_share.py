from webapp.dbase import db_session
from webapp.model import Share
from webapp import create_app

import investpy

#share_list = ['AAPL', 'MSFT', 'F', 'M', 'CL', 'TSLA', 'NVDA', 'FB', 'AMD', 'AMZN', 'QCOM', 'ZM', 'NFLX', 'ADBE', 'CSCO', 'INTC', 'DIS', 'WMT', 'JPM', 'CAT']
share_list = ['AAPL', 'MSFT']


def add_share(ap):
    one_share = Share(stock_symbol = ap['Stock Symbol'],eps = ap['EPS'],
        volume = ap['Volume'], pe_ratio = ap['P/E Ratio'], prev_close = ap['Prev. Close'],
        todays_range = replaces(ap))
    return one_share
        
    
def update_share(share_list):
    for shr in share_list:
        ap = investpy.stocks.get_stock_information(shr, 'united states', as_json=True)
        print(shr)
        one_share = Share.query.filter_by(stock_symbol = shr).first()
        if one_share:
            print(f'update {shr} to base')
            one_share.eps = ap['EPS']
            one_share.volume = ap['Volume']
            one_share.pe_ratio = ap['P/E Ratio']
            one_share.prev_close = ap['Prev. Close']
            one_share.todays_range = replaces(ap)
            print(one_share.todays_range)
            db_session.commit()
            
        else:
            print(f'add {shr} to base') 
            db_session.add(add_share(ap))
            db_session.commit()
    
    
def replaces(ap):
    """
    Функция для конвертации строки в числовой формат
    
    """
    change = ap['Todays Range']
    if ',' in change:
        change = change.replace(',', '')
    change = change.split('-')    
    change_percent = int((float(change[0]) - float(change[1]))/float(change[0])*10000)/100
    return change_percent   


app = create_app()
with app.app_context():
    update_share(share_list)  