import os
import sys
from datetime import timedelta
from dotenv import load_dotenv

sys.path.append("C:\projects\learn_project\webapp")
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'dsD243k%2lkjskad6&!@dfkslodjak'
REMEMBER_COOKIE_DURATION = timedelta(days=14)
DOLLAR_RUB = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&aqs=chrome..69i57j0i20i263i512j0i131i433i512j0i512l7.2383j1j7&sourceid=chrome&ie=UTF-8'
EURO_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&aqs=chrome..69i57j0i20i263i433i512j0i433i512l2j0i131i433i512l2j0i433i512l2j0i433i457i512j0i402.3696j1j7&sourceid=chrome&ie=UTF-8'
BITCOIN_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&newwindow=1&sxsrf=AOaemvLGEkRulk--b4S3QsNPDNoT-Ihb5Q%3A1635969344186&ei=QOmCYdfbCtKTwPAP0YivoAQ&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyBQgAEIAEMgoIABCABBCHAhAUMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEMggIABCABBDJAzIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoICAAQgAQQsQNKBAhBGABQkk5Y0FRgyVxoAXACeACAAUWIAfcDkgEBOJgBAKABAcgBCsABAQ&sclient=gws-wiz&ved=0ahUKEwjX-_3c_PzzAhXSCRAIHVHEC0QQ4dUDCA4&uact=5'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
