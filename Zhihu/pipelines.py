# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .settings import *


class ZhihuPipeline(object):
    def process_item(self, item, spider):
        return item


# 存入Mongo
class ZhihuMongoPipeline(object):
    def __init__(self):
        self.n = 1
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        # 把item对象转为字典
        tencent = dict(item)
        self.myset.insert_one(tencent)
        print(str(self.n) + "条数据保存中")
        self.n += 1
        return item
