from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from nachtmusik.items import EventItem
import re

class BigeasyportlandSpider(BaseSpider):
    name = 'bigeasyportland'
    allowed_domains = ['bigeasyportland.com']
    start_urls = ['http://bigeasyportland.com/calendar']

    def parse(self, response):
        items = []
        hxs = HtmlXPathSelector(response)
        events_xpath = (
            '//table[contains(concat(" ", @class, " "), " event ")]/tr')
        events = hxs.select(events_xpath)
        for event in events:
            date_parts = ['month', 'day']
            date_values = {}
            for date_part in date_parts:
                date_values[date_part] = event.select(
                    './/td/div[@class="%s"]/text()' % date_part).extract()
                has_date = True
            item = EventItem()
            summary = event.select('.//td[@class="summary"]')
            item['title'] = summary.select('h1/text()').extract()
            item['time'] = summary.select(
                'h1/following-sibling::*//*[contains(text(), "pm")]/text()'
            ).re(r'(?:Doors)?\s*(.*?pm)')
            item['venue'] = ['Big Easy']
            if item['title']:
                items.append(item)
        return items
