# Scrapy settings for nachtmusik project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

LOG_LEVEL = 'INFO'

BOT_NAME = 'nachtmusik'

SPIDER_MODULES = ['nachtmusik.spiders']
NEWSPIDER_MODULE = 'nachtmusik.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nachtmusik (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 1000,
}

HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_STORAGE = 'scrapy.contrib.downloadermiddleware.httpcache.FilesystemCacheStorage'
HTTPCACHE_POLICY = 'scrapy.contrib.downloadermiddleware.httpcache.DummyPolicy'
