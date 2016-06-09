# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Restaurant(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()
    address_full = scrapy.Field()
    address_street = scrapy.Field()
    address_city = scrapy.Field()
    address_zip = scrapy.Field()
    food_categories = scrapy.Field()
    menu_categories = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    link = scrapy.Field()
    date_added = scrapy.Field()
    pass
