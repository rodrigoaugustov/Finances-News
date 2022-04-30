from datetime import datetime

from scrapper.scrapper import Scrapper


class AgenciaBrasil(Scrapper):
    name = "NAME_OF_SCRAPPER"
    root_url = 'ROOT_URL_OF_WEBSITE'

    # This is the pages where the scrapper will look for the news URL. You can manually place each list item here,
    # or use some script to to navigate through pagination like the example below
    source_url = [f'https://SITEXYZ.com/page={n}' for n in range(0, 8)]

    def __init__(self):
        super().__init__(self.name, self.root_url, self.source_url)

    def get_news(self, response):
        ''' Parse page to get all news urls'''
        # The scrapper will request each url you put in SOURCE_URL and then call this function to look for news url in
        # that page. So you have to look a way to get all news urls that you want to parse

        # Customize your code here, it must return a list with urls
        urls = response.xpath('//div[@class="row my-4 d-flex "]/a/@href').getall()

        # Sometimes you get the url without the base url, so you have to concatenate. If don`t, just skip this part
        urls = [f'{self.base_url}{link}' for link in urls]
        return urls

    def get_title(self, response):
        # This function will look for the News Title.
        # Tip: Typically it's on meta properties
        title = response.xpath('//meta[@property="og:title"]/@content').get()
        return title

    def get_content(self, response):
        # This is the most challenging part. You have to look for patterns in the HTML code, to successfully extract
        # news content. You can use xpath or css methods, or whatever you want, even load another lib like beautifulsoap
        content = response.xpath('string(//div[@class="post-item-wrap"])').extract_first()
        return content.strip()

    def get_date(self, response):
        """Must return datetime format"""
        # Here you have to find a way to extract the news publish date. Sometimes it`s on meta property. Don`t forget to
        # convert to datetime format
        time = response.xpath('//meta[@property="article:published_time"]/@content').get()
        pub = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S-%I:%f')
        return pub
