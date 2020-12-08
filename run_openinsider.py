from openinsider_parser.requester import parse, logger
# from core.utils import get_logger


def main():
    logger.info('Start script')
    with open('tickers.txt', 'r') as file:
        tickers = file.read().strip()

    for ticker in tickers.split('\n'):
        parse(ticker)
    logger.info('End script')


if __name__ == '__main__':
    main()
