# -*- coding: utf-8 -*-
import scrapy
from ..items import Article_fashion


class FashionspiSpider(scrapy.Spider):
    name = 'fashionspi'
    allowed_domains = ['58fashion.com']
    start_urls = ['http://www.51fashion.com.cn/News/List1101.html']

    def parse(self, response):
        urls = response.xpath("//dd[@class='dd-4']/a/@href").extract()
        keys = response.xpath("//dd[@class='dd-4']/a/text()").extract()
        for i in range(len(urls)):
            url = response.urljoin(urls[i])
            key = keys[i]
            yield scrapy.Request(url,callback=self.Article_url)


    def Article_url(self,response):
        print(response.url)





