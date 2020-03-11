from scrapy.crawler import CrawlerProcess

from engine.ProductEngine import ProductEngine
from spider.SupremeSpider import SupremeSpider


class Main:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


if __name__ == '__main__':

    my_main = Main()
    print("I'm the main!")

    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'items.json'
    })

    process.crawl(SupremeSpider)
    process.start()
