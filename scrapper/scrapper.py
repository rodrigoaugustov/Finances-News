""" Import Modules """
import datetime

import scrapy

from src.entities.news import New
from src.services.crud import create_session
from src.utils.utils import already_exists


class Scrapper(scrapy.Spider):

    def __init__(self, name: str, root_url: str, source_url: list, **kwargs):
        self.name = name
        self.base_url = root_url
        self.source_url = source_url

        super().__init__(name, **kwargs)
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):
        for url in self.source_url:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response, **kwargs):
        # Get News URL in the page
        urls = self.get_news(response)

        # Check if that url is already on database, if not its goes on
        for url in urls:
            if not already_exists(url):
                yield response.follow(
                    url=url,
                    headers=self.headers,
                    callback=self.parse_article
                )

    def parse_article(self, response):
        """ Parse news page """
        url = response.url

        title = self.get_title(response)
        content = self.get_content(response)
        pub_date = self.get_date(response)

        new = New(
            title=title,
            content=content,
            url=url,
            published=pub_date,
            created=datetime.datetime.now(),
            source=self.name
        )

        with create_session() as session:
            session.add(new)

    def get_news(self, response):
        print("Customize your function to get news url")
        return list

    def get_title(self, response):
        print("Customize your function to get news title")
        pass

    def get_content(self, response):
        print("Customize your function to get news content")
        pass

    def get_date(self, response):
        print("Customize your function to get news publish date")
        pass
