import scrapy


class UfcResultsSpider(scrapy.Spider):
    name = "ufc_results"
    allowed_domains = ["ufcstats.com"]
    start_urls = ["http://ufcstats.com/statistics/events/completed"]

    def parse(self, response):
        pass
