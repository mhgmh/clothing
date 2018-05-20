import  requests
from lxml import etree
import pymysql as py

se = requests.session()

class article(object):

    def read_article(self):
        db = py.connect(host='140.143.237.199', user='article', password='article', db='article', charset='utf8')
        curs = db.cursor()
        allcount = "SELECT COUNT(TITLE) FROM CLOTHING"
        curs.execute(allcount)
        s = curs.fetchall()[0][0]
        print(s)
        ReadTable = "SELECT TITLE FROM CLOTHING LIMIT 10291;"
        curs.execute(ReadTable)
        tables = curs.fetchall()
        for title in tables:
            print(title)
            if 'imageUrl' in title[0]:
                title = str(title[0]).rsplit("','")[0]
            else:
                title = title[0]

                print(title)

























article.read_article('')