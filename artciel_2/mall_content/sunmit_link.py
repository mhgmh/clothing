import requests
import re

se = requests.session()

class sunmit(object):

    def Bbaidu_sunmit(url):
        Bd_url = 'http://data.zz.baidu.com/urls?site=https://www.75hb.com&token=EDUEd4qfULX3yGnV'
        headers = {
            'User-Agent': 'curl/7.12.1',
            'Host': 'data.zz.baidu.com',
            'Content-Type': 'text/plain',
            'Content-Length': '83',
        }
        se.headers.clear()
        se.headers.update(headers)
        response = se.post(Bd_url,data=url).text
        print(response)

    def Pseudo_original(content):
        headers = {
            'Cookie': 'JSESSIONID=B6DE75EECE37DABDBD5CC4C69C1F3B8F; UM_distinctid=1637c864a5f5a0-08b0bb9583ded4-336e7704-13c680-1637c864a602fb; CNZZDATA2027872=cnzz_eid%3D1896784645-1526802521-%26ntime%3D1526802521; naipanA_feixiang1799%40163.com=naipanB_a83822851',
            'Host': 'www.naipan.com',
            'Referer': 'http://www.naipan.com/member/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
        se.headers.clear()
        se.headers.update(headers)
        data = {
            'replaceNum': '0',
            'userReplaceNum': '0',
            'webContent': content,
            'amode': '0',
            'linkWeiWord':'',
            'linkWeiUrl': 'http://',
            'weiKu': '0',
            'weiMode': '0',
        }
        response = se.post('http://www.naipan.com/index.html',data=data).text
        cont = re.compile('wrap="physical">(.*?)</textarea>',re.S).findall(response)[0]
        return cont