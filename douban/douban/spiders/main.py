# _*_ coding: utf-8 _*_
# 开发人员 : Administrator
# 开发时间 : 2019/8/17 19:19
# 文件名称 : main.py
# 开发工具 : PyCharm

from scrapy import cmdline

cmdline.execute("scrapy crawl douban_spider".split())


