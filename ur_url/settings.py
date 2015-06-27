# -*- coding: utf-8 -*-

# Scrapy settings for krazywap project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'krazywap'

SPIDER_MODULES = ['krazywap.spiders']
NEWSPIDER_MODULE = 'krazywap.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'random_useragent.RandomUserAgentMiddleware': 400
}

USER_AGENT_LIST = ".\useragents.txt"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'krazywap (+http://www.yourdomain.com)'
