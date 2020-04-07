# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import  JsonItemExporter
import json
#import pymysql
from astro import settings

class AstroPipeline(object):
    def __init__(self):
        """
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DB,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASS,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()
        """

        self.fp = open("output.json", 'wb')
        self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        self.exporter.start_exporting()
 
    def open_spider(self, spider):
        pass
 
    def process_item(self, item, spider):
        """
        detail = json.dumps(item['detail'])
        insert_sql = "INSERT INTO cs_detail(name, detail, date) VALUES ('%s', '%s', '%s')" % (item['name'], detail, item['date'])
        self.cursor.execute(insert_sql)
        insert_id = self.connect.insert_id()
        self.connect.commit()
        """
        
        self.exporter.export_item(item)
        return item
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()