#coding:utf-8
import urllib2
import re
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
#链接WordPress，输入xmlrpc链接，后台账号密码
wp = Client('http://en.itmanbu.com/xmlrpc.php','cheney','Spark.1991')
post = WordPressPost()
post.content = 'a test post</br>哈哈哈'
post.post_status = 'publish'
#发送到WordPress
wp.call(NewPost(post))
print 'posts updates'