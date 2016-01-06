#/usr/bin/env python
#coding=utf8
import urllib2
import re
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
for i in content1
    if i not in exist1:
        open('contents.txt','a+').write(i+'\n')
        print i
    else:
        print i+'Already in!'
f.close()