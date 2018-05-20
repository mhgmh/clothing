# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pq

class ArtcielPipeline(object):
    def open_spider(self,spider):
        self.db = pq.connect(host='140.143.237.199',user='article',password='article',db='article',charset='utf8')
        self.curs = self.db.cursor()

    def process_item(self, item, spider):
        SHOWS = "SHOW TABLES;"
        self.curs.execute(SHOWS)
        tables = list(self.curs.fetchall())
        if len(tables) == 0:
            MKTABLE = "DROP TABLE IF EXISTS CLOTHING"
            self.curs.execute(MKTABLE)
            Mkin_table = """CREATE TABLE CLOTHING(ID INT AUTO_INCREMENT PRIMARY KEY,TITLE CHAR (200),CONTENT  LONGTEXT )"""
            self.curs.execute(Mkin_table)

        # print("暂无数据库")
        # if  tables != 'CLOTHING':
        #     MKTABLE = "DROP TABLE IF EXISTS CLOTHING"
        #     self.curs.execute(MKTABLE)
        #     Mkin_table = """CREATE TABLE CLOTHING(ID INT AUTO_INCREMENT PRIMARY KEY,TITLE CHAR (200),CONTENT  LONGTEXT )"""
        #     self.curs.execute(Mkin_table)

        data = item['content']
        # for i in item['content']:
        #     print(i)



        INTOTABLE = """INSERT INTO CLOTHING(TITLE,CONTENT)VALUES(%s,%s)"""
        self.curs.executemany(INTOTABLE,data)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.curs.close()
        self.db.close()
