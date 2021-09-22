import requests
from bs4 import BeautifulSoup
from lxml import etree
import pymysql


if __name__ == '__main__':
    url = r"http://zj.cma.gov.cn/zwxx/qxyw/202108/t20210812_3733046.html"
    responce1 = requests.get(url).content.decode("utf-8")
    html_lxml = etree.HTML(responce1)
    txtByte = html_lxml.xpath('//*[@id="zoom"]/div')[0]
    str =""
    for div in txtByte.xpath(".//text()"):
        str += div
    print(str)
    print(len(str))
    str = "\"" + str + "\""


