# -*- coding: utf-8 -*-

'''
    爬取豆瓣评分8.0以上的电影
'''

RATE = 8.0
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
writeHandle = open('result.txt', 'w+')
def wirteContent(subjects):
    rows = 0
    for subject in subjects:
        if float(subject['rate']) >RATE:
            text = subject['title']+"\t\t"+subject['url']+"\t\t"+subject['rate']+"\n"
            rows += 1
            writeHandle.write(text)
    return rows
def getSubjects(jsonString):
    data = json.loads(jsonString)
    subjects = data['subjects']
    if not subjects:
        return False
    return subjects
import urllib2
import cookielib
import random
def getUrlOpener():
    cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    user_agents = [
        'Mozilla/4.8 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.1 (Windows; U; Windows NT 7.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        'Mozilla/3.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
        'NOKIA5700/ UCWEB7.0.2.37/28/999',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
        'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
        'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
        'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
        'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
        'NOKIA5700/ UCWEB7.0.2.37/28/999',
        'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0) ',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0) ',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1;en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
        'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
        'Openwave/ UCWEB7.0.2.37/28/999',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
        'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)'
    ]
    userAgent = user_agents[random.randint(0, len(user_agents)-1)]
    opener.addheaders = [
        ("User-Agent", userAgent),
        ('Accept', '*/*'),
        ('Referee', 'https://movie.douban.com/'),
        ('Host', 'movie.douban.com'),
        ('X-Requested-With','XMLHttpRequest'),
        ('Accept-Encoding', 'gzip, deflate, sdch'),
        ('Accept-Language', 'zh-CN,zh;q=0.8'),
        ('Connection', 'keep-alive'),
        ('Cookie', 'bid=LjOMEIjy3GM; viewed="26612779"; gr_user_id=88f86520-6d10-440b-b773-0c3d804e29fc; ll="118281"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1475633878%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E8%25B1%2586%25E7%2593%25A3%26rsv_spt%3D1%26rsv_iqid%3D0x91bca6e200028729%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D7%26rsv_sug1%3D5%26rsv_sug7%3D100%22%5D; _pk_id.100001.4cf6=6de4f5fe5f84ad3d.1470060339.5.1475633878.1475573812.; _pk_ses.100001.4cf6=*; __utma=30149280.1397463788.1474694140.1475573812.1475633885.5; __utmb=30149280.0.10.1475633885; __utmc=30149280; __utmz=30149280.1475573812.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.976706976.1470060339.1475573812.1475633885.5; __utmb=223695111.0.10.1475633885; __utmc=223695111; __utmz=223695111.1475633885.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; _vwo_uuid_v2=47797DBE53FACB8D09FFD2FE37A6C24F|ebbbbb55b8f7b4b9f203c9bad52db628')
    ]
    return opener
import zlib
def spider():
    tags = ['热门', '最新', '经典','可播放', '豆瓣高分', '冷门佳片','华语','欧美','韩国',
            '日本', '动作', '喜剧', '爱情','科幻', '悬疑', '恐怖', '文艺']
    for tag in tags:
        rows = 0
        for page in range(0, 10000, 20):
            url = 'https://movie.douban.com/j/search_subjects?type=movie&tag='+tag+'&sort=recommend&page_limit=20&page_start='+str(page)
            try:
                urlOpener = getUrlOpener()
                response = urlOpener.open(url)
                content = response.read()
                if response.headers.get('Content-Encoding') == 'gzip':
                    content = zlib.decompress(content, 16 + zlib.MAX_WBITS)
                subjects = getSubjects(content)
                if not subjects:
                    break
                rows += wirteContent(subjects)
            except Exception,e:
                print url
        print '一共抓取'+tag+'标签'+str(rows)+'条'
if __name__ == '__main__':
    spider()