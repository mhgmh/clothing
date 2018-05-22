# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from lxml import etree
import re
import requests
import json
from ..items import ArtcielItem
import time

se = requests.session()


class ArticlespiSpider(scrapy.Spider):
    name = 'articlespi'
    allowed_domains = ['2298.com']
    start_urls = ['https://www.2298.com/liuxing/']

    def parse(self, response):
        urls = response.xpath("//div[@class='qh-news-head']/ul/li/a/@href").extract()
        for url in range(1,len(urls)):
            ur = 'https:'+urls[url]
            yield scrapy.Request(ur,callback=self.Read_url)




    def Read_url(self,response):
        it = ArtcielItem()
        # f = etree.HTML(response.text)
        # urls = f.xpath("//div[@class='qh-news-fr fr']/ul[@id='div_articleList']/li/a/@href")
        # for ls in urls:
        #     urls = 'https:'+ls
        #     print(urls)
        page_id = re.compile(";'>共(.*?)页</a>",re.S).findall(response.text)[0]
        Cat_id = re.compile("CategoryId = '(.*?)';").findall(response.text)[0]
        for i in range(0,int(page_id)):

            post_url = 'https://www.2298.com/Article/ajax/MyArticleNew.ashx'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            }

            se.headers.clear()
            se.headers.update(headers)
            data = {
                'cmd': 'getArticlesByCategoryIDByPage',
                'CategoryId': Cat_id,
                'nPageSize': '35',
                'nPageIndex': str(i),
            }
            Read_text = se.post(post_url,data=data).text
            titles = re.compile("'title':'(.*?)','imageUrl':'','content':'(.*?)'").findall(Read_text)
            # titles = re.compile("'articleID':'(.*?)','title':'(.*?)',").findall(Read_text)
            it['content'] = titles
            time.sleep(10)
            yield it












