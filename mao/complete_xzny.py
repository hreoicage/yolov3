import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import pymysql
import html
import re


# 获取URL除最后一段的内容（以/分割）

def transferContent(content):
    if content is None:
        return None
    else:

        stri = ""

        for c in content:

            if c == '"':

                stri += c.replace('"', '\\\"')

            elif c == "'":

                stri += c.replace("'", "\\\'")

            elif c == "\\":

                stri += "\\\\"

            else:

                stri += str(c)

    return stri


def handlepageurl(pageurl):
    if pageurl is None or pageurl == "":
        return ""
    urls = pageurl.split("/")
    tmp = ""
    for index in range(0, len(urls) - 1):
        tmp = tmp + urls[index] + "/"
    return tmp


def gettablecontent(url, pre):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    status_code = resp.status_code
    if status_code != 200:
        resp.close()
        return status_code
    else:
        soup = BeautifulSoup(resp.text, "lxml")
        div1 = soup.find("div", attrs={"id": "barrierfree_container"})
        div2 = div1.find("div", attrs={"id": "sj_head"})
        div3 = div2.find_next_sibling("div").find_next_sibling("div").find("div",
                                                                           attrs={"class": "default_pgContainer"})
        lis = div3.findAll("li")
        for li in lis:
            href = li.find_next("a").get("href").replace("./", "/")
            # 新闻标题
            title = li.find_next("a").get("title")
            # 新闻发布日期
            news_date = li.find_next("a").find_next_sibling("span").text
            tmpresp = requests.get(pre + href)
            tmpresp.encoding = "utf-8"
            tmp_status_code = tmpresp.status_code
            if tmp_status_code != 200:
                tmpresp.close()
                return tmp_status_code
            tmpsoup = BeautifulSoup(tmpresp.text, "lxml")
            tmptab = tmpsoup.find("div", attrs={"id": "barrierfree_container"}).find("table")
            tmptr = tmptab.find("div", attrs={"class": "fxgb"}).find_parent("td").find_parent("tr")
            tmpimgs = tmptab.findAll("img")
            news_content = str(tmptab)
            # print("内容", news_content)
            # news_content = re.escape(news_content)
            conn = pymysql.connect(host='192.168.3.131', user="root", passwd="maitian123", db="testDB", port=3306)
            cursor = conn.cursor()
            news_content = transferContent(news_content)
            sqlStr = "INSERT INTO test (news_content) VALUES (" + "\"" + news_content + "\"" + ")"
            print(sqlStr)
            cursor.execute(sqlStr)
            conn.commit()
            cursor.close()
            conn.close()
            # print("内容", tmptab)

            # 通过当前页地址获取图片地址前缀
            pageurl = handlepageurl(tmpresp.url)
            for img in tmpimgs:
                oldsrc = img.get("oldsrc")
                # 获取新的图片地址
                newsrc = pageurl + oldsrc
                # 新闻中图片地址替换为爬取后地址，可修改为本项目图片存放的地址
                img["src"] = newsrc
                # 新闻中国图片下载
                urlretrieve(newsrc, "../images/" + oldsrc)
            tmptr.clear()
            # 新闻内容HTML，仅包含table代码段
            content = tmptab
            tmpresp.close()
        resp.close()
        return status_code


if __name__ == "__main__":
    news_url = "http://zj.cma.gov.cn/zwxx/qxyw/index"
    pre_fix = "http://zj.cma.gov.cn/zwxx/qxyw"
    post_fix = ".html"
    tmpurl = news_url + post_fix
    count = 0
    while True:
        status = gettablecontent(tmpurl, pre_fix)
        if status != 200:
            break
        else:
            count = count + 1
            tmpurl = news_url + "_" + str(count) + post_fix
