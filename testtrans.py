#/usr/bin/env python
#coding=utf8
import httplib
import md5
import urllib
import random
import urllib2
import re
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#得到html的源码
def gethtml(url1):
    #伪装浏览器头部
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(
    url = url1,
    headers = headers
    )
    html = urllib2.urlopen(req).read()
    return html
#得到目标url源码
code1 = gethtml('http://www.qiushibaike.com/8hr/page/1')
#提取内容
content1 = re.findall('<div class="content">\n\n(.*)\n<!--',code1)
#追加的方式记录采集来的内容
f = open('contents.txt','a+')
#读取txt中的内容
exist = f.read()
for i in content1:
    #如果不在就追加新的内容
    #open('contents.txt','a+').write(i+'\n')
    contentdec1 = i
    #百度翻译api
    appid = '20151113000005349'
    secretKey = 'osubCEzlGjzvw8qdQc41'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    fromLang = 'auto'
    toLang = 'jp'
    salt = random.randint(32768, 65536)
    q = contentdec1
    sign = appid+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    print q
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        readres = response.read();
        data = json.loads(readres)
        trans_result = data['trans_result']
        dst = trans_result[0]['dst']+'<p>From:<em><a href="http://www.qiushibaike.com">糗事百科 – 超搞笑的原创糗事分享社区</a></em></p>'
        print dst[:20]
        #data_string = json.dumps(dst,ensure_ascii=False)
        #print data_string[:20]
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    print 'posts updates'
f.close()