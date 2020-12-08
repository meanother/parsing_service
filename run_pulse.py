from pulse_parser.requester import parse
from core.utils import get_logger

logger = get_logger('pulse-service')


def main():
    logger.info('Start script')
    with open('tickers.txt', 'r') as file:
        tickers = file.read().strip()

    for ticker in tickers.split('\n'):
        parse(ticker, 150)
    logger.info('End script')


if __name__ == '__main__':
    main()
