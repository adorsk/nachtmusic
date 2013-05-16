from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from nachtmusik.items import EventItem
import re

class PortcityblueSpider(BaseSpider):
    name = 'portcityblue'
    allowed_domains = ['portcityblue.com']
    start_urls = ['http://portcityblue.com/calendar/']

    def parse(self, response):
        items = []
        hxs = HtmlXPathSelector(response)
        events_xpath = '//span[@class="calnk"]'
        events = hxs.select(events_xpath)
        month_year = hxs.select(
            '//td[@class="calendar-month"]/text()').extract().pop()
        month, year = month_year.split()
        for event in events:
            item = EventItem()
            day = event.select(
                'ancestor::td[@class="day-with-date"]/span/text()'
            ).extract()
            if day:
                day = day.pop()
            else:
                continue
            item['title'] = event.select(
                './/*[@class="event-title"]/text()').extract().pop()
            event_time = event.select(
                'a/span/text()[1]').extract()
            if event_time and re.search('am|pm', event_time[0]):
                event_time = event_time.pop()
            else:
                continue
            item['time'] = "%s %s %s %s" % (day, month, year, event_time)
            item['venue'] = ['Port City Blue']
            items.append(item)
        return items
