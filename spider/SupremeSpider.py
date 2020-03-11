import scrapy

class SupremeSpider(scrapy.Spider):
    name = "supreme_spider"
    start_urls = ['https://supremenewyork.com/shop/all']

    def parse(self, response):
        for article in response.xpath("//div[@class='turbolink_scroller']/article//div/a"):

            if "sold_out_tag" not in article.extract():
                yield {
                    'article': article.xpath('@href').extract()
                }
