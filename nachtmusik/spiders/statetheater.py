from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from nachtmusik.items import EventItem

class StatetheaterportlandSpider(BaseSpider):
    name = 'statetheatreportland'
    allowed_domains = ['statetheatreportland.com']
    start_urls = ['http://www.statetheatreportland.com/listing/']

    def parse(self, response):
        items = []
        hxs = HtmlXPathSelector(response)
        events_xpath = '//div[contains(concat(" ", @class, " "), " vevent ")]'
        events = hxs.select(events_xpath)
        for event in events:
            item = EventItem()
            item['title'] = event.select('h1/a/text()').extract()
            item['time'] = event.select(
                'h2[@class="times"]//span[contains(concat(" ",@class, " "),'
                ' " dtstart ")]/span/@title').extract()
            item['venue'] = ['State Theatre']
            items.append(item)
        return items
