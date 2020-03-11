import scrapy

class SupremeSpider(scrapy.Spider):
    SUPREME_WEB_PAGE = 'https://www.supremenewyork.com'
    name = "supreme_spider"
    start_urls = [SUPREME_WEB_PAGE + '/shop/all']

    def parse(self, response):
        for article in response.xpath("//div[@class='turbolink_scroller']/article//div/a"):
            if "sold_out_tag" not in article.extract():
                #yield {
                #    'article': SupremeSpider.SUPREME_WEB_PAGE + article.xpath('@href').extract()[0]
                #}
                yield scrapy.Request(url=SupremeSpider.SUPREME_WEB_PAGE + article.xpath('@href').extract()[0], callback=self.parse_page2, meta={'is_sold_out': 'false'})

    def parse_page2(self, response):
        item = response.meta['is_sold_out']
        # add whatever extra details you want to item

        yield {
            'article': response.xpath('//div[@id="details"]/h1/text()').get(),
            'color': response.xpath('//div[@id="details"]//p[@class="style protect"]/text()').get()
        }