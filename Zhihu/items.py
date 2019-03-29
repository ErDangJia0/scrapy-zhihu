# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    headline = scrapy.Field()
    gender = scrapy.Field()
    url_token=scrapy.Field()
    question = scrapy.Field()
    topics = scrapy.Field()
