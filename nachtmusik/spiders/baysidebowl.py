from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from nachtmusik.items import EventItem
import re

class BaysidebowlSpider(BaseSpider):
    name = 'baysidebowl'
    allowed_domains = ['baysidebowl.com']
    start_urls = ['http://baysidebowl.com/events/']

    def parse(self, response):
        """ TODO """
        items = []
        hxs = HtmlXPathSelector(response)
        return items
