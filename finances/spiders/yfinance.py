import scrapy


class YfinanceSpider(scrapy.Spider):
    name = 'yfinance'
    allowed_domains = ['https://br.financas.yahoo.com/']
    start_urls = ['http://https://br.financas.yahoo.com//']

    def parse(self, response):
        pass
