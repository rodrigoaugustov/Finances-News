import scrapy
import re

from datetime import datetime

from src.entities.news import New
from src.services.crud import create_session
from src.utils.utils import already_exists


class InvestingSpider(scrapy.Spider):
    name = 'brinvesting'
    base_url = 'https://br.investing.com'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):
        urls = [
            f'https://br.investing.com/news/stock-market-news/{n}' for n in range(1, 10)
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response, **kwargs):
        urls = response.xpath('//a[contains(@class, "title")]/@href').getall()
        for link in urls:
            if 'https' not in link:
                url = f'{self.base_url}{link}'
                if not already_exists(url):
                    yield response.follow(url=url, headers=self.headers, callback=self.parse_article)

    def parse_article(self, response):
        url = response.url
        title = response.xpath('//title/text()').get()
        title = re.sub(r'Por.*', '', title).strip()
        divs = response.css('.WYSIWYG.articlePage p')
        content = ' '.join([i.xpath('string()').extract_first() for i in divs])
        time = response.css('.contentSectionDetails span::text').get()
        if "(" in time:
            time = time.split('(')[1].split(')')[0]
        time = datetime.strptime(time, '%d.%m.%Y %H:%M')

        new = New(
            title=title,
            content=content,
            url=url,
            published=time,
            source=self.name
        )

        with create_session() as s:
            s.add(new)
