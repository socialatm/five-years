import scrapy


class TottSpider(scrapy.Spider):
    name = "tott"
    allowed_domains = ["ufcstats.com"]
    start_urls = ["http://ufcstats.com/statistics/events/completed"]

    def parse(self, response):
        pass
