import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FrenchstauPipeline(object):
    def process_item(self, item, spider):
        return item
