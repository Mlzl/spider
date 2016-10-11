#-*- encoding:utf-8 -*-
#铎哥的任务
import urllib2
import cookielib
import urllib
import re
import xlwt

class Spider:
    LOGIN_URL = 'http://www.safetyme.cn/Login.shtml'
    SID_URL = "http://www.safetyme.cn//a/exam.shtml?method=index"

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.cj = cookielib.LWPCookieJar()
        self.install_opener()
        self.paper = []

    def install_opener(self):
        cookie_support = urllib2.HTTPCookieProcessor(self.cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

    def get_response(self, url, post_data=None, header={}):
        if post_data:
            post_data = urllib.urlencode(post_data)
        request = urllib2.Request(url, data=post_data, headers=header)

        response = urllib2.urlopen(request)
        return response

    def write_excel(self):
        wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = wbk.add_sheet(str(self.name), cell_overwrite_ok=True)
        row = 1
        text = ['题型', '问题', '选项', '答案']
        clo = 0
        for t in text:
            sheet.write(0, clo, t)
            clo += 1
        for t in self.paper:
            sheet.write(row, 0, t['type'])
            sheet.write(row, 1, t['question'])
            sheet.write(row, 2, t['s'])
            sheet.write(row, 3, t['answer'])
            row += 1
        wbk.save(str(self.name) + '.xlsx')

    def parse_content(self, content):
        p1 = "\<span style=\"color: green;font-weight:bold;\"\>\[(.*?)\]</span>"  # 题型
        p2 = "<span>(.*?)\<span id=\"(.*?)\""  # 题目
        p4 = "yyvalit=\"A\"\>(.*?)\<\/label\>"  # A
        p5 = "yyvalit=\"B\"\>(.*?)\<\/label\>"  # B
        p6 = "yyvalit=\"C\"\>(.*?)\<\/label\>"  # C
        p11 = re.findall(p1, content)
        p22 = re.findall(p2, content)
        p22 = iter(p22)
        p44 = re.findall(p4, content)
        p44 = iter(p44)
        p55 = re.findall(p5, content)
        p55 = iter(p55)
        p66 = re.findall(p6, content)
        p66 = iter(p66)
        result = []
        for t in p11:
            question = next(p22)
            p3 = "\"" + question[1] + "\":\"(.*?)\""  # 答案
            answer = re.findall(p3, content)
            one = {'type': t, 'question': question[0], 'answer': answer}
            if t == '判断题':
                one['s'] = '对，错'
            else:
                one['s'] = "A:" + next(p44) + "B" + next(p55) + "C" + next(p66)
            result.append(one)
        return result

    def parse_sid(self, content):
        pattern = "onclick=\"openPaper\(\'(.*?)\'"
        return re.findall(pattern, content)

    def run(self):
        print "爬取用户%d开始" % self.name
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
            'Referee': self.LOGIN_URL
        }
        post_data = {
            'card_no': self.name,
            'card_pwd': self.pwd
        }
        login_response = self.get_response(self.LOGIN_URL, post_data, headers)
        login_cookie = self.get_login_cookie()
        if not login_cookie:
            print "user " + self.name + " login failed.response:" + login_response
        headers['Cookie'] = login_cookie
        spider_sid_response = self.get_response(self.SID_URL, header=headers)
        sids = self.parse_sid(spider_sid_response.read())
        print "一共%d份试卷" % len(sids)
        self.parse_paper(sids, headers)
        self.write_excel()
        print "一共爬取%d条问题" % len(self.paper)
    def parse_paper(self, sids,headers={}):
        for sid in sids:
            paper_url = "http://www.safetyme.cn//a/exam.shtml?method=showPaper&id=" + sid
            response = self.get_response(paper_url, header=headers)
            content = response.read().decode('gbk').encode('utf-8')
            qANDa = self.parse_content(content)
            self.paper.extend(qANDa)

    def get_login_cookie(self):
        return_cookie = []
        for cookie in self.cj:
            if cookie.name == 'JSESSIONID':
                return_cookie.append(cookie.name+"="+cookie.value)
        if not return_cookie:
            return False
        return ";".join(return_cookie)

accounts = [
    {'name': 156024163, 'password': 731644},
    {'name': 156304832, 'password': 169776},
    {'name': 156304831, 'password': 125524},
    {'name': 156347080, 'password': 309933},
]
if __name__ == '__main__':
    for account in accounts:
        spider = Spider(account['name'], account['password'])
        spider.run()



