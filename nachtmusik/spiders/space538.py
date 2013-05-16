from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from nachtmusik.items import EventItem
import re

class Space538Spider(BaseSpider):
    name = 'space538'
    allowed_domains = ['space538.org']
    start_urls = ['http://space538.org/events/upcoming']

    def parse(self, response):
        items = []
        hxs = HtmlXPathSelector(response)
        events_xpath = (
            '//div[contains(concat(" ", @class, " "), " event-music ")]')
        events = hxs.select(events_xpath)
        for event in events:
            item = EventItem()
            item['title'] = event.select(
                './/*[@class="title"]/a/text()').extract()
            item['time'] = event.select(
                './/*[@class="date-display-single"]/@content').extract()
            item['venue'] = ['Space']
            items.append(item)
        return items
