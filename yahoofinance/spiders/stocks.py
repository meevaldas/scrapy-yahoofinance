import scrapy


class StocksSpider(scrapy.Spider):
    name = "stocks"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com"]

    def parse(self, response):
        pass
