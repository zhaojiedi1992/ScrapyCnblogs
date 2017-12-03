# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapycnblogsItem
from scrapy.exceptions import DropItem
import re
import json


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['http://www.cnblogs.com/zhaojiedi1992/default.html?page=1']

    def get_postid_from_edit_url(self,edit_url):
        if edit_url is None:
            return None
        #"https://i.cnblogs.com/EditPosts.aspx?postid=7954278"
        self.logger.debug("-----------"+edit_url +"--------------------------------------")
        re_post_id=re.compile(".*=([0-9]+)")
        post_id=re_post_id.match(edit_url)
        if post_id:
            return post_id.groups()[0]

    def parse(self, response):
        for it in response.css(".postTitle2::attr(href)").extract():
            yield scrapy.Request(it,callback=self.parse_one_page,dont_filter=True,meta={"refer":response.url})
        next_page= response.css(".topicListFooter a:contains('下一页')::attr(href)").extract_first()
        yield scrapy.Request(next_page,callback=self.parse,dont_filter=True,meta={"refer":response.url})

        #response=response.replace(encoding="gbk")
    def parse_one_page(self,response):
        item = ScrapycnblogsItem()
        item["url"] = response.url
        item["title"]=response.css("#cb_post_title_url::text").extract_first()
        #item["content"]=response.css("#cnblogs_post_body::text").extract_first()
        item["edit_url"]=response.css("#topics > div > div.postDesc > a:nth-child(5)::attr(href)").extract_first()
        item["post_id"]=self.get_postid_from_edit_url(item["edit_url"])
        item["refer_url"]=response.meta["refer"]
        #if item["post_id"] is None:
        #    return None
        #http://www.cnblogs.com/mvc/blog/ViewCountCommentCout.aspx?postId=7954278
        request = scrapy.Request("http://www.cnblogs.com/mvc/blog/ViewCountCommentCout.aspx?postId="+item["post_id"],callback=self.parse_view_count,dont_filter=True)
        request.meta['item'] = item
        yield request


    def parse_view_count(self,response):
        item=response.meta["item"]
        item["view_count"] = response.text
        request = scrapy.Request("http://www.cnblogs.com/mvc/blog/GetComments.aspx?blogApp=zhaojiedi1992&pageIndex=0&postId="+item["post_id"],callback=self.parse_comment_count,dont_filter=True)
        request.meta['item'] = item
        yield request

    def parse_comment_count(self,response):
        item=response.meta["item"]
        commnet_json=json.loads(response.text)
        item["comment_count"]=commnet_json["commentCount"]
        yield item