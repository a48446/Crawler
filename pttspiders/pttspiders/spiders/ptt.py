# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from pttspiders.items import PttspidersItem


class pttspiders(scrapy.Spider):
    name = 'ptt'
    start_urls = [
        'https://www.ptt.cc/bbs/index.html'
    ]
    domain = 'https://www.ptt.cc'
    def parse(self, response):
        # print(response.text)

        soup = BeautifulSoup(response.body, 'lxml')
        Linktags = soup.find_all('a', href = re.compile(r"index"))
        print(Linktags[0])
        print(len(Linktags))
        for tag in Linktags:
            print(tag.text.strip().replace('\n',' '))
            soup = BeautifulSoup(str(tag), 'lxml')
            url = self.domain + tag.get('href')
            boardName = soup.select('div.board-name')[0].text
            push = soup.select('div.board-nuser')[0].text
            boardClass = soup.select('div.board-class')[0].text
            boardTitle = soup.select('div.board-title')[0].text
            print(url)
            print(boardName)
            print(push)
            print(boardClass)
            print(boardTitle)
            
            item = PttspidersItem()
            item[boardlink]=url
            item[boardname]=boardName
            item[TotalPush]=push
            item[boardClass]=boardClass
            item[boardtitle]=boardTitle
            yield(item)

        