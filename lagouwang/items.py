# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouwangItem(scrapy.Item):
    pk=scrapy.Field()
    page=scrapy.Field()
    positionname=scrapy.Field()
    city=scrapy.Field()
    company=scrapy.Field()
    salary=scrapy.Field()
    request=scrapy.Field()
    companykinds=scrapy.Field()
    provide=scrapy.Field()
    welfare=scrapy.Field()
