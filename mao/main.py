# conding=utf-8
import sys

import pymysql
import requests
from bs4 import BeautifulSoup
from lxml import etree


def gettablecontent(url, pre):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    print(resp.status_code)
    if resp.status_code != 200:
        return resp.status_code
    else:
        soup = BeautifulSoup(resp.text, "lxml")
        div1 = soup.find("div", attrs={"id": "barrierfree_container"})
        div2 = div1.find("div", attrs={"id": "sj_head"})
        div3 = div2.find_next_sibling("div").find_next_sibling("div").find("div",
                                                                           attrs={"class": "default_pgContainer"})
        lis = div3.findAll("li")

        for li in lis:
            href = li.find_next("a").get("href").replace("./", "/")
            title = li.find_next("a").get("title")
            news_date = li.find_next("a").find_next_sibling("span").text
            print("url", href)
            print("标题", title)
            print("时间", news_date)
            print(pre + href)
            responce1 = requests.get(pre + href).content.decode("utf-8")
            html_lxml = etree.HTML(responce1)
            txtByte = html_lxml.xpath('//*[@id="zoom"]/div')[0]
            str1 = ""
            for div in txtByte.xpath(".//text()"):
                #print(div)
                str1 += div

            str1 = "\"" + str1 + "\""
            href = "\"" +pre+ href + "\""
            news_date = "\"" +news_date + "\""
            title = "\"" + title + "\""
            conn = pymysql.connect(host='139.159.225.130', user="biye", passwd="123456", db="biye", port=53306)
            cursor = conn.cursor()
            sqlStr = "INSERT INTO test (url,time,content,title) VALUES ( " + href +"," +news_date+ "," + str1 +","+title+ ")"
            #sqlStr = 'INSERT INTO test (id,url,time,content,title) VALUES (%s,%s,%s,%s,%s)'
            # print(sqlStr)
            count = cursor.execute(sqlStr)
            print(count)
            conn.commit()
            conn.close()  # 先关闭游标

        return resp.status_code


if __name__ == "__main__":
    news_url = "http://zj.cma.gov.cn/zwxx/qxyw/index"
    pre_fix = "http://zj.cma.gov.cn/zwxx/qxyw"
    post_fix = ".html"
    tmpurl = news_url + post_fix
    count = 0
    while True:
        print("页面url", tmpurl)
        status = gettablecontent(tmpurl, pre_fix)
        if status != 200:
            break
        else:
            count = count + 1
            tmpurl = news_url + "_" + str(count) + post_fix
