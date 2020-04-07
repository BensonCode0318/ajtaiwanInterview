import scrapy
import time
import re,time
from astro.items import AstroItem

class astroSprider(scrapy.Spider):
    name = 'astroSprider'
    allowed_domains = ['click108.com.tw']
    start_urls = ['http://astro.click108.com.tw']

    def parse(self, response):
        item = AstroItem()
        for starBox in response.css('div.STAR12_BOX ul > li'):
            time.sleep(1)
            item['name'] = starBox.css('a::text').extract()
            meta = {'name':item['name']}
            url = starBox.css('a::attr(href)')[0].extract().split('*')
            yield scrapy.Request(url[1],callback=self.parse_article,meta = meta)

    def parse_article(self,response):
        meta = response.meta
        url = response.css('script::text').extract()[0].lstrip().replace('location.href="','').replace('";','')
        yield scrapy.Request(url,callback=self.parse_content,meta = meta)

    def parse_content(self,response):
        item = AstroItem()
        name = response.meta['name'][0]
        detail = {}
        score = response.css('div.TODAY_CONTENT p > span::text').extract()
        explain = response.css('div.TODAY_CONTENT p::text').extract()
        for i in range(len(score)):
            detail[score[i][:4]] = score[i][4:]
            detail[score[i][:4]+'說明'] = explain[i]
        item['name'] = name
        item['detail'] = detail
        item['date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        meta = {
            'date':item['date'],
            'name':item['name'],
            'detail':item['detail']
        }
        return meta