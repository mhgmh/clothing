import requests
import pymysql as py
from artciel.mall_content.Published_articles import Task_url
import time
se = requests.session()


class article(object):


    def read_article(self):
        db = py.connect(host='140.143.237.199', user='article', password='article', db='article', charset='utf8')
        curs = db.cursor()
        # Tatol_number = "SELECT COUNT(*) FROM CLOTHING"
        # curs.execute(Tatol_number)
        # number = curs.fetchall()[0][0]

        ReadTable = "SELECT ID,TITLE,CONTENT FROM CLOTHING LIMIT 1;"
        curs.execute(ReadTable)
        tables = list(curs.fetchall())

        for i in tables:
            lists = list(i)
            if 'imageUrl' in lists[1]:
                title = str(lists[1]).rsplit("','")[0]
            else:
                title = lists[1]
            content = lists[2]
            State = Task_url.submit(title,content)
            print('当前文章:'+title+"发布状态为:"+State)
            delete = "DELETE FROM CLOTHING WHERE ID = '{}'".format(lists[0])
            curs.execute(delete)
            db.commit()
        curs.close()
        db.close()







def main():
    tis = 0
    while True:
        article.read_article('')
        if tis >= 5:
            print('当前文章已发布5篇，即将开始延时,延时周期为5分钟~')
            time.sleep(1800)
            tis = 0
        else:
            tis += 1
            print("当前的tis值为:" + str(tis))


if __name__ == '__main__':
    main()