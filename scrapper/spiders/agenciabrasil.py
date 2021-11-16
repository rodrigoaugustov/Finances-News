import scrapy
import re

from datetime import datetime

from src.entities.news import New
from src.services.crud import create_session
from src.utils.utils import already_exists


class InvestingSpider(scrapy.Spider):
    name = 'agenciaBrasil'
    base_url = 'https://agenciabrasil.ebc.com.br'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):
        urls = [
            f'https://agenciabrasil.ebc.com.br/economia?page={n}' for n in range(0, 8)
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response, **kwargs):
        urls = response.xpath('//div[@class="row my-4 d-flex "]/a/@href').getall()
        for link in urls:
            url = f'{self.base_url}{link}'
            if not already_exists(url):
                yield response.follow(url=url, headers=self.headers, callback=self.parse_article)

    def parse_article(self, response):
        url = response.url
        title = response.xpath('//meta[@property="og:title"]/@content').get()
        content = response.xpath('string(//div[@class="post-item-wrap"])').extract_first()
        time = response.xpath('//meta[@property="article:published_time"]/@content').get()
        time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S-%I:%f')

        new = New(
            title=title,
            content=content,
            url=url,
            published=time,
            source=self.name
        )

        with create_session() as s:
            s.add(new)
