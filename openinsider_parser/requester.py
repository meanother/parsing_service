import requests
from bs4 import BeautifulSoup as bs
import traceback

from core.db import insert
from core.utils import (
    parse_time,
    headers,
    logger_time,
    get_logger,
)

SRC_URL = 'http://openinsider.com/screener?s={}&o=&pl=&ph=&ll=&lh=&fd=0&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=10000000&page=1'

logger = get_logger('openinsider-service')


def get_request(insider_url, ticker):
    logger.info(f'Get request with tickername: {ticker}')
    session = requests.Session()
    data = session.get(insider_url.format(ticker), headers=headers, stream=True)
    return data.text


@logger_time
def get_data(html):
    soup = bs(html, 'lxml')
    rows = soup.find('table', class_='tinytable').find('tbody').find_all('tr')
    for i in rows:
        row = i.find_all('td')
        data = {
            'x': row[0].text.strip(),
            'filing_date': row[1].text.strip(),
            'trade_date': row[2].text.strip(),
            'ticker': row[3].text.strip(),
            'insider_name': row[4].text.strip(),
            'insider_title': row[5].text.strip(),
            'trade_type': row[6].text.strip(),
            'price_raw': row[7].text.strip(),
            'price_formatted': row[7].text.strip()[1:],
            'qty': row[8].text.strip(),
            'owned_raw': row[9].text.strip(),
            'owned_formatted': row[9].text.strip().replace(',', ''),
            'own': row[10].text.strip(),
            'value_raw': row[11].text.strip(),
            'value_formatted': row[11].text.strip().replace('$', '').replace(',', ''),
            'one_d': row[12].text.strip(),
            'one_w': row[13].text.strip(),
            'one_m': row[14].text.strip(),
            'six_m': row[15].text.strip(),
            'parse_time': parse_time,
        }
        logger.info(data)
        insert('openinsider', data)


def parse(ticker):
    try:
        get_data(get_request(SRC_URL, ticker))
    except AttributeError as e:
        logger.error(f'cant get page info, maybe wrong ticker: {str(e) + traceback.format_exc()}')
