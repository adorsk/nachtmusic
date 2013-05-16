from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from nachtmusik.items import EventItem

class OnelongfellowsquareSpider(BaseSpider):
    name = 'onelongfellowsquare'
    allowed_domains = ['onelongfellowsquare.com']
    start_urls = ['http://www.onelongfellowsquare.com/Results.asp?category=2']

    def parse(self, response):
        items = []
        hxs = HtmlXPathSelector(response)
        events_xpath = '//table[@id="tableSearchResults"]/tr/td[2]'
        events = hxs.select(events_xpath)
        for event in events:
            item = EventItem()
            item['title'] = event.select('h2/text()').extract()
            item['time'] = event.select('span[@class="dt2"]/text()').extract()
            item['description'] = event.select('p/text()').extract()
            item['venue'] = ['One Longfellow Square']
            items.append(item)
        return items
