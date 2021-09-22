import requests

import requests


def login():
    url = "http://171.221.203.127:30037/cas/login?service=%2Fjobhoursmanage%2Fj_security_check&__t=1624278474522&locale=zh_CN"
    params = {
        "username": "SF4467",  # input标签下的name
        "_password": "cdsf@119"  # input标签下的name
    }

    html = session.post(url, data=params)
    print(html.status_code)

    print(html.cookies.get_dict())
    req = "http://171.221.203.127:30037/jobhoursmanage/bmsApi/getUserInfoById"
    he
    get_id = session.post(req)
    print("getid status", get_id.status_code)
    print(get_id.text)


def add_task_time():
    DayUrl = "http://171.221.203.127:30037/jobhoursmanage/projectTaskTime/addProjectTaskTime"
    DAy_data = {"projectTaskTimes[0].productIds": "302001",
                "projectTaskTimes[0].description": "x",
                "projectTaskTimes[0].workContentId": "116",
                "projectTaskTimes[0].realConsume": "7.5",
                "projectTaskTimes[0].hours": "0",
                "projectTaskTimes[0].taskDateStr": "2021-06-20",
                "projectTaskTimes[0].typeId": "5003",
                "projectTaskTimes[0].projectId": "a48f3ee5-8559-4f56-ae59-8f859b275a80",
                "projectTaskTimes[0].businessTripFlag": "1"
                }
    header = {"Cookie": 'JSESSIONID=87A373829AB14354A88AA05E6FAE503B;'
                        ' org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; lan=zh_CN',
              "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
    html = session.post(DayUrl, data=DAy_data, headers=header)
    status_code = html.status_code
    print("status_code", status_code)
    return status_code


def getlist():
    url = "http://171.221.203.127:30037/jobhoursmanage/projectTaskTime/getProjectTaskTimeList"


if __name__ == '__main__':
    session = requests.session()
    login()

"""
url = "http://171.221.203.127:30037/jobhoursmanage/projectTaskTime/addProjectTaskTime"
data = {"projectTaskTimes[0].productIds": "302001",
        "projectTaskTimes[0].description": "x",
        "projectTaskTimes[0].workContentId": "116",
        "projectTaskTimes[0].realConsume": "7.5",
        "projectTaskTimes[0].hours": "0",
        "projectTaskTimes[0].taskDateStr": "2021-06-20",
        "projectTaskTimes[0].typeId": "5003",
        "projectTaskTimes[0].projectId": "a48f3ee5 - 8559 - 4f56 - ae59 - 8f859b275a80",
        "projectTaskTimes[0].businessTripFlag": "1"
        }
header = {"Cookie": 'JSESSIONID=87A373829AB14354A88AA05E6FAE503B;'
                    ' org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; lan=zh_CN',
          "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
html = requests.get(url, data=data, headers=header)
print(html.text)
"""
