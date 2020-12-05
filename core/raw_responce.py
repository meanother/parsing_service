import requests
import re
from bs4 import BeautifulSoup as bs
from typing import Dict, List, Tuple, AnyStr


def get_html(url: AnyStr) -> AnyStr:
    session = requests.Session()
    data = session.get(url)
    return data.text


def get_data(html: AnyStr):
    soup = bs(html, 'lxml')
    posts = soup.find('div', {'data-qa-file': 'Container'}).find('div')\
        .find('div').find('div', {'class': re.compile(r'InfinityScroll__root\w+')})\
        .find_all('div', {'class': re.compile(r'PulsePost__container\w+')})
    for post in posts:
        name = post.find('div', {'data-qa-file': 'PulsePostAuthor'}).find('a').get('href')[23:-1]
        text = post.find('div', {'data-qa-file': 'PulsePostCollapsed'}).text
        likes = post.find('div', {'class': re.compile(r'PulsePostBody__postReaction\w+')})\
            .find('div', {'data-qa-file': 'PulsePostBody'}).text.replace('\xa0', '').replace('нравится', '')
        time = post.find('div', {'data-qa-file': 'PulsePostAuthor'})\
            .find('div', {'class': re.compile(r'PulsePostAuthor__inserted\w+')}).text
        data = {
            'Name': name,
            'Likes': likes,
            'Text': text,
            'Time': time,
        }
        print(data)
    print(len(posts))

# get_soup(get_html('https://www.tinkoff.ru/invest/stocks/JOBS/pulse/'))
