from core.requester import parse


def main():
    with open('tickers.txt', 'r') as file:
        tickers = file.read().strip()

    for ticker in tickers.split('\n'):
        parse(ticker, 150)


if __name__ == '__main__':
    main()
