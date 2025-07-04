import scrapy


class StatsSpider(scrapy.Spider):
    name = "stats"
    allowed_domains = ["ufcstats.com"]
    start_urls = ["http://ufcstats.com/statistics/events/completed"]

    def parse(self, response):
        pass
