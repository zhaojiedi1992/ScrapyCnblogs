# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapycnblogsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    refer_url=scrapy.Field()
    url= scrapy.Field()
    edit_url=scrapy.Field()
    title=scrapy.Field()
    #content=scrapy.Field()
    post_id=scrapy.Field()
    view_count=scrapy.Field()
    comment_count=scrapy.Field()
    