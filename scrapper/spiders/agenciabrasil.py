from datetime import datetime

from scrapper.scrapper import Scrapper


class AgenciaBrasil(Scrapper):
    name = "AgenciaBrasil"
    root_url = 'https://agenciabrasil.ebc.com.br'
    source_url = [f'https://agenciabrasil.ebc.com.br/economia?page={n}' for n in range(0, 8)]

    def __init__(self):
        super().__init__(self.name, self.root_url, self.source_url)

    def get_news(self, response):
        ''' Parse page to get all news urls'''
        # must return a list with urls
        urls = response.xpath('//div[@class="row my-4 d-flex "]/a/@href').getall()
        urls = [f'{self.base_url}{link}' for link in urls]
        return urls

    def get_title(self, response):
        title = response.xpath('//meta[@property="og:title"]/@content').get()
        return title

    def get_content(self, response):
        content = response.xpath('string(//div[@class="post-item-wrap"])').extract_first()
        return content.strip()

    def get_date(self, response):
        """Must return datetime format"""
        time = response.xpath('//meta[@property="article:published_time"]/@content').get()
        pub = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S-%I:%f')
        return pub
