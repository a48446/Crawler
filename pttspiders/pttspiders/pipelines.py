# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo

# class PttspidersPipeline:
#     def process_item(self, item, spider):
#         item['push'] = int(item['push'])
#         return item

# class MongoDBPipeline:
#     print('Pipline')
    
#     def open_spider(self,spider):
#         db_url = spider.settings.get('MONGODB_URI')
#         print(db_url)
#         db_name = spider.settings.get('MONGODB_DB_NAME')
#         print(db_name)
#         db_coll= spider.settings.get('MONGODB_DB_COL')
#         print(db_coll)
#         db_client= spider.settings.get('mongodb://localhost:27017')

#         self.coll = db_client[db_name][db_coll]
    
#     def process_item(self,item,spider):
#         self.insert_article(item)
#         return item
    
#     def insert_ararticle(self,item):
#         item = dict(item)
#         print(item)
#         self.coll.insert_one(item)
    
#     def close_spider(self,spider):
#         self.db_client.close()