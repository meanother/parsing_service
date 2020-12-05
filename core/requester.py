import re
import time
from typing import Dict, List, Tuple, AnyStr
from datetime import datetime

import requests
from pytz import timezone

from .utils import (
    parse_time,
    headers,
    logger,
    url,
    logger_time,
)
from .db import insert


def get_cursor_number(url: str, ticker: str, cursor='9999999') -> Dict:
    session = requests.Session()
    logger.info(f'Get cursor number from {url.format(ticker, cursor)}')
    data = session.get(url.format(ticker, cursor), headers=headers, stream=True)
    logger.info(f"Prev cursor number is {data.json()['payload']['nextCursor']}")
    return data.json()['payload']['nextCursor']


def get_data_from_api(url: str, ticker: str, cursor: str) -> None:
    session = requests.Session()
    data = session.get(url.format(ticker, cursor), headers=headers, stream=True)
    logger.info(f"User agent: {headers['User-Agent']}")
    logger.info(f'Current url: {url.format(ticker, cursor)}')
    for post in data.json()['payload']['items']:

        instruments = [f"ticker: {item['ticker']}, name: {item['briefName']}, price: {item['price']}" for item in post['instruments']]
        hashtags = re.findall(r'#\w+', post['text'], re.MULTILINE | re.DOTALL)
        utc_time = datetime.strptime(post['inserted'], '%Y-%m-%dT%H:%M:%S.%f%z')\
            .replace(tzinfo=timezone('utc')).strftime("%Y-%m-%d %H:%M:%S")

        my_data = {
            'ticker': ticker,
            'post_date': post['inserted'],
            'post_date_utc': utc_time,
            'hashtags': ', '.join(hashtags),
            'cursor': data.json()['payload']['nextCursor'],
            'comments': post['commentsCount'],
            'likes': post['likesCount'],
            'username': post['nickname'],
            'text': post['text'],
            'instruments': ' :: '.join(instruments),
            'parse_time': parse_time,
        }
        logger.info(my_data)
        insert('pulse_parser', my_data)


@logger_time
def parse(ticker, count):
    logger.info(f'Run parser with params ticker: {ticker}, count: {count}')
    maximum = '999999999'
    for _ in range(round(count/30)):
        get_data_from_api(url, ticker, maximum)
        time.sleep(0.5)
        maximum = get_cursor_number(url, ticker, maximum)
        time.sleep(0.2)
