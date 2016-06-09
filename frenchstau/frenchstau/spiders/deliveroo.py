from bs4 import BeautifulSoup as bs
from lxml import etree
import requests
import scrapy
from frenchstau.items import Restaurant
import time
import random
import datetime

class Deliveroo(scrapy.Spider):
    name = "deliveroo"
    allowed_domains = ["deliveroo.fr"]
    start_urls = []
    sitemaps = ["https://deliveroo.fr/sitemap.xml"]
    for sitemap in sitemaps:
        tags = bs(requests.get(sitemap).text, "lxml").find_all("url")
        for tag in tags:
            resto_link = tag.findNext("loc").text
            start_urls.append(resto_link)
    start_urls = start_urls[0:15]
    def parse(self, response):
        try:
            datetime = int(str(int(time.time()*100))) #Don't change!
            random.seed(123)
            item = Restaurant()
            item['id'] = str(datetime)

            item['name'] = response.selector.xpath('//*[@class="restaurant-details"]/h1/text()').extract()[0].strip()
            item['food_categories'] = response.selector.xpath('//div[@class="restaurant-meta"]/ul/li[1]/span[2]/text()').extract()

            address = response.selector.xpath('//div[@class="restaurant-meta"]/ul/li[3]/span[2]/text()').extract()[0]
            if address != "":
                item['address_full'] = address
            else:
                item['address_full'] = response.selector.xpath('//div[@class="restaurant-meta"]/ul/li[4]/span[2]/text()').extract()[0]

            address = item['address_full'].split(", ")
            item['address_street'] = address[0]
            item['address_city'] = address[1]
            item['address_zip'] = address[2]

            item['image_urls'] = response.selector.xpath('//*[@class="cvr"]/@style').extract()[0].replace("background-image:url(","").replace(");","")

            item['menu_categories'] = response.selector.xpath('//ul[@class="no-ui menu--toc"]/li/a/text()').extract()
            for i in range(0, len(item['menu_categories'])):
                item['menu_categories'][i] = item['menu_categories'][i].strip()

            item['link'] = response.url
            item['date_added'] = unicode(str(time.strftime("%d/%m/%Y %H:%M:%S")), "utf-8")

            yield item
        except IndexError as e:
            return