# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PttHotcrawlerItem(scrapy.Item):
    boardlink = scrapy.Field()
    boardname = scrapy.Field()
    TotalPush = scrapy.Field()
    boardClass = scrapy.Field()
    boardtitle = scrapy.Field()

