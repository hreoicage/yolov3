from selenium import webdriver


def login(url):
    browser = webdriver.Chrome()
    browser.get(url)


if __name__ == '__main__':
    # 页面url
    login_url = "http://171.221.203.127:30037/jobhoursmanage/static/index.html#/"
    login(login_url)
