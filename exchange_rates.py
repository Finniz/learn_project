import requests
from bs4 import BeautifulSoup
import config

def dollar_value():
    full_page = requests.get(config.DOLLAR_RUB, headers=config.headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert[0].text

def euro_value():
    full_page = requests.get(config.EURO_RUB, headers=config.headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert[0].text

def bitcoin_value():
    full_page = requests.get(config.BITCOIN_RUB, headers=config.headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert[0].text

if __name__ == "__main__":
    dollar_value()
    euro_value()
    bitcoin_value()