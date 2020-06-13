# -*- coding: utf-8 -*-
import scrapy


class AdidasSpider(scrapy.Spider):
    name = 'adidas'
    allowed_domains = ['www.adidas.com']
    start_urls = ['http://www.adidas.com/']

    def parse(self, response):
        pass
