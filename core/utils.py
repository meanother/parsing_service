import logging
import os
import time
from datetime import datetime
from functools import wraps

from fake_useragent import UserAgent

url = 'https://www.tinkoff.ru/api/invest-gw/social/v1/post/instrument/{}?limit=30&appName=invest&platform=web&cursor={}'

parse_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s [%(levelname)s] %(name)s %(funcName)s - %(message)s',
#     filename=f'{dir}/pulse-service.log',
# )
# logger = logging.getLogger(__name__)


def get_logger(filename):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s %(funcName)s - %(message)s',
        filename=f'{dir}/{filename}.log',
    )
    logger = logging.getLogger(__name__)
    return logger


ua = UserAgent()

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': ua.random,
    'Accept': '*/*',
}


def logger_time(func):
    @wraps(func)
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        result_time = time.time() - start
        # logger.info(f'function: {func.__name__} is worked {str(round(result_time, 2))} seconds')
        return result

    return timer
