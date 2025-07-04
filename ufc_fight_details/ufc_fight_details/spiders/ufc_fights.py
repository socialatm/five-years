import scrapy


class UfcFightsSpider(scrapy.Spider):
    name = "ufc_fights"
    allowed_domains = ["ufcstats.com"]
    start_urls = ["http://ufcstats.com/statistics/events/completed"]

    def parse(self, response):
        pass
