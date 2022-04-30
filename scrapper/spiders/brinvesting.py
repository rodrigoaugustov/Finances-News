import json

from datetime import datetime

from scrapper.scrapper import Scrapper


class BrInvesting(Scrapper):
    name = "BrInvesting"
    root_url = 'https://br.investing.com'
    source_url = [f'https://br.investing.com/news/stock-market-news/{n}' for n in range(1, 10)]

    def __init__(self):
        super().__init__(self.name, self.root_url, self.source_url)

    def get_news(self, response):
        ''' Parse page to get all news urls'''
        # must return a list with urls
        urls = response.xpath('//a[contains(@class, "title")]/@href').getall()
        urls = [f'{self.base_url}{link}' if 'https' not in link else link for link in urls]
        return urls

    def get_title(self, response):
        title = response.xpath('//meta[@property="og:description"]/@content').get()
        return title

    def get_content(self, response):
        divs = response.css('.WYSIWYG.articlePage p')
        content = ' '.join([i.xpath('string()').extract_first() for i in divs])
        return content.strip()

    def get_date(self, response):
        """Must return datetime format"""
        time = json.loads(response.xpath(
            '//script[@type="application/ld+json"]//text()'
        ).get())['dateCreated']
        pub = datetime.strptime(time.split('+')[0], '%Y-%m-%dT%H:%M:%S')
        return pub
