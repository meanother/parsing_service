from core.requester import parse
from core.utils import logger


def main():
    logger.info('Start script')
    with open('tickers.txt', 'r') as file:
        tickers = file.read().strip()

    for ticker in tickers.split('\n'):
        parse(ticker, 150)
    logger.info('End script')


if __name__ == '__main__':
    main()
