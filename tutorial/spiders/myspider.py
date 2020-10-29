import scrapy
from scrapy.exceptions import DontCloseSpider
from scrapy import signals
import random


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'

    def parse(self, response):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("crawling url: %s" % response.url)
        next_url = "{}/{}".format(response.url, random.randint(1, 100))
        print("will yield url %s" % next_url)
        yield scrapy.Request(next_url)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = cls(*args, **kwargs)
        spider._set_crawler(crawler)
        spider.crawler.signals.connect(spider.spider_idle, signal=signals.spider_idle)
        return spider

    def spider_idle(self):
        self.log("Spider idle signal caught.")
        raise DontCloseSpider

