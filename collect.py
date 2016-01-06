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
import time
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
reload(sys)
sys.setdefaultencoding('utf-8')
time1 = time.time()
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
code2 = gethtml('http://www.qiushibaike.com/8hr/page/2')
#提取内容
content1 = re.findall('<div class="content">\n\n(.*)\n<!--',code1)
content2 = re.findall('<div class="content">\n\n(.*)\n<!--',code2)
#追加的方式记录采集来的内容
f1 = open('contents1.txt','a+')
f2 = open('contents2.txt','a+')
#读取txt中的内容
exist1 = f1.read()
exist2 = f2.read()
def trans(i,lang):
    #百度翻译api设置
    appid = '20151113000005349'
    secretKey = 'osubCEzlGjzvw8qdQc41'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    fromLang = 'auto'
    toLang = lang
    salt = random.randint(32768, 65536)
    q = i
    sign = appid+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        readres = response.read();
        data = json.loads(readres)
        trans_result = data['trans_result']
        dst = trans_result[0]['dst']+'<p>From <em><a href="http://www.qiushibaike.com">糗事百科 – 超搞笑的原创糗事分享社区</a></em></p>'
        title = dst[:20]
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    #链接WordPress，输入xmlrpc链接，后台账号密码
    wp = Client('http://'+lang+'.itmanbu.com/xmlrpc.php','username','password')
    post = WordPressPost()
    post.title = title
    post.content = dst
    post.post_status = 'publish'
    #发送到WordPress
    wp.call(NewPost(post))
    time.sleep(3)
    print lang+'posts updates'

for i in content1:
    if i not in exist1:
        #如果不在就追加新的内容
        open('contents1.txt','a+').write(i+'\n')
        trans(i,'en')
        trans(i,'jp')
        trans(i,'kor')
        trans(i,'fra')
        trans(i,'spa')
        trans(i,'th')
        trans(i,'ara')
        trans(i,'ru')
        trans(i,'pt')
        trans(i,'de')
        trans(i,'it')
        trans(i,'el')
        trans(i,'nl')
        trans(i,'pl')
        trans(i,'bul')
        trans(i,'est')
        trans(i,'dan')
        trans(i,'fin')
        trans(i,'cs')
        trans(i,'rom')
        trans(i,'slo')
        trans(i,'swe')
        trans(i,'hu')
        print 'Page1 finished'
    else:
        print 'No posts updates'
for i in content2:
    if i not in exist2:
        #如果不在就追加新的内容
        open('contents2.txt','a+').write(i+'\n')
        trans(i,'en')
        trans(i,'jp')
        trans(i,'kor')
        trans(i,'fra')
        trans(i,'spa')
        trans(i,'th')
        trans(i,'ara')
        trans(i,'ru')
        trans(i,'pt')
        trans(i,'de')
        trans(i,'it')
        trans(i,'el')
        trans(i,'nl')
        trans(i,'pl')
        trans(i,'bul')
        trans(i,'est')
        trans(i,'dan')
        trans(i,'fin')
        trans(i,'cs')
        trans(i,'rom')
        trans(i,'slo')
        trans(i,'swe')
        trans(i,'hu')
        print 'page2 finished'
    else:
        print 'No posts updates'
f.close()
time2 = time.time()
print time2 - time1