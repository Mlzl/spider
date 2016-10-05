# -*- coding: utf-8 -*-
# 爬取煎蛋的妹子图
import urllib2
import cookielib
import re
import zlib
import time
import random
URL = 'http://jandan.net/ooxx/page-'
SUFFIX = ''
def getUrl():
    for page in range(1, 2152):#2152
        url = URL+str(page)+SUFFIX
        yield url
def parseImg(content):
    imgs = re.findall('http://ww4.sinaimg.cn/large/(.*?\.jpg)', content)
    return imgs

def getUrlOpener(url='http://jandan.net/ooxx'):
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
        ('Referee', 'http://jandan.net/ooxx'),
        ('Host', 'jandan.duoshuo.com'),
        ('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
        ('Accept-Encoding', 'gzip, deflate, sdch'),
        ('Accept-Language', 'zh-CN,zh;q=0.8'),
        ('Connection', 'keep-alive'),
        ('Referee', url),
        ('Cookie', 'duoshuo_unique=0d42fa33a6416b09')
    ]
    return opener

def spider():
    opener = getUrlOpener()
    for url in getUrl():
        print 'start spider '+url
        try:
            response = opener.open(url)
            content = response.read()
            if response.headers.get('Content-Encoding') == 'gzip':
                content = zlib.decompress(content, 16 + zlib.MAX_WBITS)
            imgUrl = parseImg(content)
            downLoadImg(imgUrl, opener)
            time.sleep(1)
        except urllib2.HTTPError,e:
            if not again(url):
                print 'stop when spider '+url
                break
        opener = getUrlOpener(url)
    print 'end '+url
readUrlHandle = open('url.txt', 'r')
againTime = []
def again(url):
    opener = getUrlOpener('https://www.baidu.com')
    sleepTime = 1
    if len(againTime) > 30:
        return False
    print 'start again spider ' + url + ' sleep '+str(sleepTime)+' second'
    try:
        response = opener.open(url)
        content = response.read()
        if response.headers.get('Content-Encoding') == 'gzip':
            content = zlib.decompress(content, 16 + zlib.MAX_WBITS)
        imgUrl = parseImg(content)
        downLoadImg(imgUrl, opener)
        time.sleep(1)
    except urllib2.HTTPError, e:
        againTime.append('a')
        time.sleep(sleepTime)
        again(url)
    del againTime[:]
    return True
def readUrlImg():
    return readUrlHandle.readlines()

def WriteImg(filename, content):
    dir = random.randrange(1, 5)
    handle = open(str(dir)+'/'+filename, 'wb')
    handle.write(content)
    handle.close()
def downLoadImg(imgUrls , opener):
    for url in imgUrls:
        newUrl = 'http://ww4.sinaimg.cn/large/'+url
        imgContent = opener.open(newUrl)
        WriteImg(url, imgContent.read())
        time.sleep(0.1)

def destruct():
    writeUrlHandle.close()
    writeHtmlHandle.close()

import os
def mkdir():
    for i in range(1, 5):
        if not os.path.exists(str(i)):
            os.mkdir(str(i))
import threading
if __name__ == '__main__':
    mkdir()
    spider()
    pass
destruct()

