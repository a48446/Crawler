# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class PttHotcrawlerPipeline(object):
    def Process_item(self,item,spider):
        item['TotalPush'] = int(item['TotalPush'])
        return item