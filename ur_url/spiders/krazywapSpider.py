from scrapy.contrib.spiders import  CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item, Field
import scrapy
from krazywap.items import KrazywapItem

domain_name = "gamezwap.net"
str_url = "http://"+domain_name+"/"
substr1 = "1"
class KrazySpider(CrawlSpider):
    name = "krazySpider1"
    allowed_domains = [domain_name]
    start_urls = [str_url]
    rules = [
        #Rule(SgmlLinkExtractor(allow=(),), follow=True, callback='parse_item'),
        #Rule(SgmlLinkExtractor(deny = ('http://www.pakheaven.org/', )), ),
        Rule(SgmlLinkExtractor(), callback='parse_item',follow=True),
        Rule(SgmlLinkExtractor()),
]
    fname = 0

    def parse_item(self, response):
        name1 = response.url
        file_format = name1[-4:]
        f = open('myfile.txt','a')
        f.write(name1+'\n') # python will convert \n to os.linesep
        f.close()
        if file_format == ".jar" or file_format == ".3gp" or file_format == ".mp4":
            last_slash_index = name1.split('&name=')
            myitem = KrazywapItem()
            myitem['name'] = last_slash_index[1]
            myitem['link'] = response.url
            return myitem
   
        ''' 
        ''' 






