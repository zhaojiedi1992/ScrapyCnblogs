# ScrapyCnblogs
抓取指定用户的cnblogs信息

## 注意点
修改bnblogs.py文件中的zhaojiedi1992为你要爬取的博客用户名即可


## 环境需要
* scrapy

## 运行方法

```cmd
E:\ZhaojiediProject\github\ScrapyCnblogs\ScrapyCnblogs>dir
 驱动器 E 中的卷是 新加卷
 卷的序列号是 D20B-7155

 E:\ZhaojiediProject\github\ScrapyCnblogs\ScrapyCnblogs 的目录

2017/12/03  13:09    <DIR>          .
2017/12/03  13:09    <DIR>          ..
2017/12/02  22:50    <DIR>          .vscode
2017/12/03  13:09            72,025 items.csv
2017/12/03  13:09           102,558 items.jl
2017/12/03  13:09           111,953 items.json
2017/12/03  13:09            96,348 items.marsha
2017/12/03  13:09           116,193 items.pickle
2017/12/03  13:09           104,385 items.pprint.jl
2017/12/02  23:11               511 items.py
2017/12/03  13:09           117,156 items.xml
2017/12/02  19:38             1,911 middlewares.py
2017/12/02  19:43               582 other.txt
2017/12/03  13:06             3,994 pipelines.py
2017/12/03  13:09         1,267,800 scrapy.log
2017/12/03  13:09             3,557 settings.py
2017/12/02  23:02    <DIR>          spiders
2017/05/19  05:10                 0 __init__.py
2017/12/03  13:09    <DIR>          __pycache__
              14 个文件      1,998,973 字节
               5 个目录 388,466,298,880 可用字节

E:\ZhaojiediProject\github\ScrapyCnblogs\ScrapyCnblogs>scrapy list
cnblogs

E:\ZhaojiediProject\github\ScrapyCnblogs\ScrapyCnblogs>scrapy crawl cnblogs
```


## 样例输出结果

### json导出的部分结果

```json
[
{
    "url": "http://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi_linux_020_lamp.html",
    "title": "LAMP环境快速搭建",
    "edit_url": "https://i.cnblogs.com/EditPosts.aspx?postid=6785436",
    "post_id": "6785436",
    "refer_url": "http://www.cnblogs.com/zhaojiedi1992/default.html?page=1",
    "view_count": "21",
    "comment_count": 0
},
{
    "url": "http://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi_linux_019_https.html",
    "title": "基于openssl搭建https服务器",
    "edit_url": "https://i.cnblogs.com/EditPosts.aspx?postid=6770342",
    "post_id": "6770342",
    "refer_url": "http://www.cnblogs.com/zhaojiedi1992/default.html?page=1",
    "view_count": "30",
    "comment_count": 0
}]
```

### xml导出的部分结果

```xml
<items>
<item><url>http://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi_linux_020_lamp.html</url><title>LAMP环境快速搭建</title><edit_url>https://i.cnblogs.com/EditPosts.aspx?postid=6785436</edit_url><post_id>6785436</post_id><refer_url>http://www.cnblogs.com/zhaojiedi1992/default.html?page=1</refer_url><view_count>21</view_count><comment_count>0</comment_count></item><item><url>http://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi_linux_019_https.html</url><title>基于openssl搭建https服务器</title><edit_url>https://i.cnblogs.com/EditPosts.aspx?postid=6770342</edit_url><post_id>6770342</post_id><refer_url>http://www.cnblogs.com/zhaojiedi1992/default.html?page=1</refer_url><view_count>30</view_count><comment_count>0</comment_count></item>
</itmes>
```

### ppring格式导出的部分结果

```json
{'comment_count': 0,
 'edit_url': 'https://i.cnblogs.com/EditPosts.aspx?postid=6785436',
 'post_id': '6785436',
 'refer_url': 'http://www.cnblogs.com/zhaojiedi1992/default.html?page=1',
 'title': 'LAMP环境快速搭建',
 'url': 'http://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi_linux_020_lamp.html',
 'view_count': '21'}
{'comment_count': 0,
 'edit_url': 'https://i.cnblogs.com/EditPosts.aspx?postid=6770342',
 'post_id': '6770342',
 'refer_url': 'http://www.cnblogs.com/zhaojiedi1992/default.html?page=1',
 'title': '基于openssl搭建https服务器',
 'url': 'http://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi_linux_019_https.html',
 'view_count': '30'}
```
