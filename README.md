# Python-
学习并精通Python爬虫
这是一个基础的爬虫。需要两部分来完成。
1.获取网页：http://www.pythonscraping.com/pages/page1.html 使用Python中的requests库.
requests库是一个非常好用爬虫第三方库
基本用法:
requests.get ：获取网页的主要方法，对应HTTP中的GET
requests.head ： 获取网页的头信息，对应HTTP中的HEAD
requests.post : 向网页中提交POST请求的方法，对应HTTP的POST
requests.put : 向网页中提交PUT请求的方法，对应HTTP的PUT
requests.patch ： 向网页提交局部修改请求，对应HTTP的PATCH
requests.DELETE ： 向网页提交删除请求，对应HTTP的DELETE
其中get方法最为常用，返回一个response对象，而我们使用的html.text是response对象的属性之一，返回页面内容。
2.用BeautifulSoup库解析网页内容，找到title。

其中我们使用了Python的容错机制，try....except....当网址错误或网页内容中没有title标签时，就会启用except，返回错误。
