#!/usr/bin/env python
# Python3

'''
selenium的使用
'''

from selenium import webdriver

try:
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    browser = webdriver.Firefox(firefox_options=fireFoxOptions)

    browser.get('http://www.baidu.com')
    #print(brower.page_source)
    print(brower.title)
finally:
    try:
        brower.close()
    except:
        pass