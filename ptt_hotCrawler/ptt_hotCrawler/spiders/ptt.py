# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from ptt_hotCrawler.items import PttHotcrawlerItem

class PttSpider(scrapy.Spider):
    count_page = 1
    name = 'ptt'
    allowed_domains = ['www.ptt.cc/']
    start_urls = ['https://www.ptt.cc/bbs/hotboards.html']
    def parse(self, response):
        for q in response.css('div.b-ent'):
            item = {
                'boardlink': 'https://www.ptt.cc/' +q.css('a.board::attr(href)').extract_first(),
                'boardname': q.css('div.board-name::text').extract_first(),
                'boardClass':q.css('div.board-class::text').extract_first(),
                'boardtitle':q.css('div.board-title::text').extract_first(),
                'TotalPush': q.css('div.board-nuser > span.hl::text').extract_first(),
            }
            yield(item)
        next_page_url = response.css('div.action-bar > div.btn-group > a.btn::attr(href)')[3].extract()
        if (next_page_url) and (self.count_page < 10):
            self.count_page = self.count_page + 1 
            new = response.urljoin(next_page_url) 
        else:   
            raise  CloseSpider('close it')
        yield scrapy.Request(new, callback = self.parse, dont_filter = True)
        
           
        # # print(response.text)

        # soup = BeautifulSoup(response.body, 'lxml')
        # Linktags = soup.find_all('a', href = re.compile(r"index"))
        # print(Linktags[0])
        # print(len(Linktags))
        # for tag in Linktags:
        #     # print(tag.text.strip().replace('\n',' '))
        #     soup = BeautifulSoup(str(tag), 'lxml')
        #     url = self.domain + tag.get('href')
        #     boardName = soup.select('div.board-name')[0].text
        #     push = soup.select('div.board-nuser')[0].text
        #     boardClass = soup.select('div.board-class')[0].text
        #     boardTitle = soup.select('div.board-title')[0].text
        #     print(url)
        #     print(boardName)
        #     print(push)
        #     print(boardClass)
        #     print(boardTitle)
        #     item = PttItem(boardlink=url , boardName=boardName, TotalPush=push, boardClass=boardClass, boardTitle=boardTitle )
        #     yield item
