import scrapy
from scrapy.crawler import CrawlerProcess

from yahoofinance.spiders.stocks import StocksSpider


def main():
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "stocks.json": {"format": "json"},
            },
        }
    )

    process.crawl(StocksSpider)
    process.start()  # the script will block here until the crawling is finished


if __name__ == "__main__":
    main()
