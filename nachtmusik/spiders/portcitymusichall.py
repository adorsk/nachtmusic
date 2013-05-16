from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from nachtmusik.items import EventItem

class PortcitymusichallSpider(BaseSpider):
    name = 'portcitymusichall'
    allowed_domains = ['portcitymusichall.com']
    start_urls = ['http://portcitymusichall.com/events']

    def parse(self, response):
        items = []
        hxs = HtmlXPathSelector(response)
        events_xpath = '//article[@class="event"]'
        events = hxs.select(events_xpath)
        for event in events:
            item = EventItem()
            item['title'] = event.select('aside/hgroup/h1/a/text()').extract()
            event_date = event.select(
                './/*[contains(text(), "Event Date:")]'
                '/following-sibling::span[1]/time/@datetime').extract().pop()
            event_time = event.select(
                './/*[contains(text(), "Event Starts:")]'
                '/following-sibling::span[1]/text()').extract().pop()
            item['time'] = "{} {}".format(event_date, event_time)
            item['venue'] = ['Port City Music Hall']
            items.append(item)
        return items
