import scrapy


class UfcEventsSpider(scrapy.Spider):
    name = "ufc_events"
    allowed_domains = ["ufcstats.com"]
    start_urls = ["http://ufcstats.com/statistics/events/completed"]

    def parse(self, response):
        pass
