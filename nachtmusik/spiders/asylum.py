from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from nachtmusik.items import EventItem
import re

class AsylumSpider(BaseSpider):
    name = 'asylum'
    allowed_domains = ['portlandasylum.com']
    start_urls = ['http://portlandasylum.com/concerts/']

    def parse(self, response):
        items = []
        hxs = HtmlXPathSelector(response)
        events_xpath = '//div[@class="productcol"]'
        events = hxs.select(events_xpath)
        for event in events:
            item = EventItem()
            date_title = event.select(
                './/*[@class="wpsc_product_title"]/text()').extract().pop()
            date, title = re.findall(
                ur'(.*)\s*\u2013\s*(.*)', date_title, re.UNICODE)[0]
            item['title'] = title
            item['time'] = date
            item['venue'] = 'Asylum'
            items.append(item)
        return items
