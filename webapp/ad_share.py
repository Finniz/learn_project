from dbase import db_session
from model import Share
import investpy

share_list = ['AAPL', 'MSFT', 'F', 'M', 'CL', 'TSLA', 'NVDA', 'FB', 'AMD', 'AMZN', 'QCOM', 'ZM', 'NFLX', 'ADBE', 'CSCO', 'INTC', 'DIS', 'WMT', 'JPM', 'CAT']

def add_share(share_list):
    for share in share_list:
        ap = investpy.stocks.get_stock_information(share, 'united states', as_json=True)

        first_share = Share(stock_symbol = ap['Stock Symbol'],eps = ap['EPS'],
            volume = ap['Volume'], pe_ratio = ap['P/E Ratio'], prev_close = ap['Prev. Close'])
        db_session.add(first_share)
        db_session.commit()

add_share(share_list)        