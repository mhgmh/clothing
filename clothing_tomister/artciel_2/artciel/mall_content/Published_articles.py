import requests
from lxml import etree
from artciel.mall_content.sunmit_link import sunmit as sun
se = requests.session()
class Task_url(object):

    def submit(title,content):
        sucont = sun.Pseudo_original(content)
        params = {
            'title':(None,title),
            'article_cat':(None,'1007'),
            'article_type':(None,'0'),
            'is_open':(None,'1'),
            'sort_order':(None,'50'),
            'link_url':(None,'http://'),
            'FCKeditor1':(None,sucont),
            'category_name':(None,'请选择分类'),
            'category_id':(None,'0'),
            'brand_id':(None,'0'),
            'submit':(None,'确定'),
            'act':(None,'insert'),
        }

        headers = {
            'cookie': 'ECSCP[lastfilterfile]=23A0E66; ECSCP[lastfiltersql]=U0VMRUNUIGEuKiAsIGFjLmNhdF9uYW1lIEZST00gYGZfNzVoYl9jb21gLmBkc2NfYXJ0aWNsZWAgQVMgYSBMRUZUIEpPSU4gYGZfNzVoYl9jb21gLmBkc2NfYXJ0aWNsZV9jYXRgIEFTIGFjIE9OIGFjLmNhdF9pZCA9IGEuY2F0X2lkIFdIRVJFIDEgIE9SREVSIGJ5IGEuYXJ0aWNsZV9pZCBERVND; ECSCP[lastfilter]=a%253A9%253A%257Bs%253A7%253A%2522keyword%2522%253Bs%253A0%253A%2522%2522%253Bs%253A6%253A%2522cat_id%2522%253Bi%253A0%253Bs%253A7%253A%2522sort_by%2522%253Bs%253A12%253A%2522a.article_id%2522%253Bs%253A10%253A%2522sort_order%2522%253Bs%253A4%253A%2522DESC%2522%253Bs%253A12%253A%2522record_count%2522%253Bs%253A3%253A%2522969%2522%253Bs%253A9%253A%2522page_size%2522%253Bi%253A15%253Bs%253A4%253A%2522page%2522%253Bi%253A1%253Bs%253A10%253A%2522page_count%2522%253Bd%253A65%253Bs%253A5%253A%2522start%2522%253Bi%253A0%253B%257D; province=6; city=76; district=0; street=1; street_area=1; session_id_ip=125.70.189.105_56c3679cb2828e90a4fe0ba78fce9a8b; __jsluid=17ec2d2bc70b9742126cf87e9895c8e0; UM_distinctid=1622a067c2dab-063a1db422d315-32637b06-13c680-1622a067c2e763; CNZZDATA1273120948=637645911-1521123489-null%7C1521123489; bdshare_firstime=1521124121690; _umdata=55F3A8BFC9C50DDAB3E481180856696BD071BFB56AB36ECA099506EF3C6831FF81F6354903FBAB58CD43AD3E795C914C645DF6384835AE407CC4C225A9F84C33; Z41o_2132_ulastactivity=ca43nPvJk%2FPjKe9dde01MrlHzr1iGQMJiC4GMCsyB0Cy9po7wcSL; Z41o_2132_nofavfid=1; Z41o_2132_lastcheckfeed=1%7C1522854523; ECS[history]=26582%2C34875%2C24856%2C35386%2C34711%2C35378%2C34603%2C29978; ECS[list_history]=26582%2C34875%2C24856%2C35386%2C34711%2C35378%2C34603%2C29978; CNZZDATA1273495606=583202017-1526395721-%7C1526395721; Z41o_2132_visitedfid=58D47D2D42; yunsuo_session_verify=f779c6c6f841fecab90805645eea8dd8; ECS[visit_times]=1; Hm_lvt_d37804ec3d9bfa562610cdb6525fadd5=1526297870,1526402446,1526402452,1526733241; adminStartHome=cookieValue; real_ipd=171.209.103.136; dsc_real_ip=171.209.103.136; ECSCP_ID=4e3c0324f17953201a0e5062fb7d30cc3456e47f; dscUrl=article.php%3Fact%3Dlist; dscActionParam=menuplatform%7C03_article_list',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
        url = 'https://www.75hb.com/admin/article.php'
        se.headers.clear()
        se.headers.update(headers)
        response = se.post(url,data = params).text
        if '文章已经添加成功' in response:
            articlelist = se.get('https://www.75hb.com/admin/article.php?act=list').text
            f = etree.HTML(articlelist)
            urlid = str(f.xpath("//div[@class='list-div']/table/tbody/tr/td/div[@class='tDiv a3']/a/@href")[0]).rsplit('=')[1]
            url = 'https://www.75hb.com/article-{}.html'.format(urlid)
            sun.Bbaidu_sunmit(url)
            return '文章发布成功'
        else:
            return '文章发布失败'

