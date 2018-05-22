# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArtcielItem(scrapy.Item):
    content = scrapy.Field()


class Article_fashion(scrapy.Item):
    key = scrapy.Field()
    url = scrapy.Field()

