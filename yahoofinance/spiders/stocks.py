import scrapy
from scrapy import Selector
from itemloaders import ItemLoader
from yahoofinance.items import YahoofinanceItem
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/']

    def parse(self, r):
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.get(self.start_urls[0])
        driver.implicitly_wait(2)
        # Uncomment the below code if there is accept the cookies policy
        # driver.find_element(By.NAME, "agree").click()
        # time.sleep(3)
        driver.find_element(By.XPATH, "//button[@title='next']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@title='next']").click()
        time.sleep(1)
        response = driver.page_source
        selector = Selector(text=response)
        containers = selector.xpath("//li[contains(@id,'marketsummary-itm')]")
        for c in containers:
            item = ItemLoader(item=YahoofinanceItem(), response=response, selector=c)
            item.add_xpath("name", ".//a/text()")
            item.add_xpath("change", ".//fin-streamer/span/text()")
            item.add_xpath("timestamp", str(datetime.now().timestamp()))
            yield item.load_item()
        driver.quit()
