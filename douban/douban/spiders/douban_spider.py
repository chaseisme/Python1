# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        print(movie_list)
        nums = 0
        for m_item in movie_list:
            nums += 1
            douban_items = DoubanItem()
            print("这是第{}个，抓取的内容为：{}".format(nums,m_item))
            # print("再次匹配到的内容为：",m_item.xpath(".//div[@class='info']//span[@class='title'][1]/text()").extract_first())
            #获取电影的排行名次
            douban_items["movie_num"] = m_item.xpath(".//div[@class='item']//em/text()").extract_first()
            #获取电影名称
            douban_items["movie_name"] = m_item.xpath(".//div[@class='info']//span[@class='title'][1]/text()").extract_first()
            #获取电影的星级
            douban_items["movie_star"] = m_item.xpath(".//div[@class='star']//span[@class='rating_num']/text()").extract_first()
            #获取电影的描述信息
            douban_items["movie_des"] = m_item.xpath(".//p[@class='quote']//span[@class='inq']/text()").extract()
            yield douban_items

        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link =next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)
