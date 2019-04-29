#!/usr/bin/env python3
# -*- coding: utf-8 -*-


MAINBODY = '''{
    "Comment": "Add new task by referring exist configuation! Only Firefox, Chrome, PhantomJS supported.",
    "Name": "SDFPlusRC",
    "Initialization": {
        "Comment": "No more than 5 threads on 1GB RAM",
        "MaxThreads": 5,
        "SearchTimeout": 60,
        "Browser": "PhantomJS",
        "CSVTitle": "ICT"
    },
    "Tasks": []
}'''

LINKEDIN = '''
{
    "Name": "cloud Linkedin",
    "Url": "https://www.linkedin.com/search/results/people/?keywords=cloud&origin=SWITCH_SEARCH_VERTICAL",
    "Locating": {
        "ByType": "css selector",
        "Location": "h3.search-results__total"
    },
    "Login": {
        "LoginUrl": "https://www.linkedin.com/",
        "Username": {
            "ByType": "id",
            "Location": "login-email",
            "Input": "jira_it_1@126.com"
        },
        "Password": {
            "ByType": "id",
            "Location": "login-password",
            "Input": "abcD-1223"
        },
        "LogonFlag": {
            "ByType": "id",
            "Location": "jobs-nav-item"
        }
    }
}
'''

WWWINDEED = '''
{
    "Name": "cloud US indeed",
    "Url": "http://www.indeed.com/q-cloud-l-United-States-jobs.html",
    "Locating": {
        "ByType": "xpath",
        "Location": "//*[@id=\\"searchCount\\"]"
    },
    "Filter": "%s.split('of')[-1]"
}
'''

CNINDEED = '''
{
    "Name": "cloud CN indeed",
    "Url": "http://cn.indeed.com/q-cloud-l-United-States-jobs.html",
    "Locating": {
        "ByType": "xpath",
        "Location": "//*[@id=\\"searchCount\\"]"
    },
    "Filter": "%s.split('共')[-1]"
}
'''

JPINDEED = '''
{
    "Name": "cloud JP indeed",
    "Url": "http://jp.indeed.com/q-cloud-l-United-States-jobs.html",
    "Locating": {
        "ByType": "xpath",
        "Location": "//*[@id=\\"searchCount\\"]"
    },
    "Filter": "%s.split('中')[0]"
}
'''

ZHAOPIN = '''
{
    "Name": "SDN ZHAOPIN",
    "Url": "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&kw=SDN&p=1&isadv=0",
    "Locating": {
        "ByType": "css selector",
        "Location": "span.search_yx_tj"
    }
}
'''

NASDAQ = '''
{
    "Name": "nasdaq tsla",
    "Url": "http://www.nasdaq.com/symbol/tsla/historical",
    "Locating": {
        "ByType": "xpath",
        "Location": "//*[@id=\\"quotes_content_left_pnlAJAX\\"]/table/tbody/tr[2]/td[5]"
    }
}
'''

RUINDEED = '''
{
    "Name": "RU indeed",
    "Url": "https://ru.indeed.com/jobs-in-russia",
    "Locating": {
        "ByType": "xpath",
        "Location": "//*[@id=\\"searchCount\\"]"
    },
    "Filter": "%s.replace(' ','').split('из')[0]"
}
'''


import sys, json


# Main thread
if len(sys.argv) < 2:
	print("Usage: " + sys.argv[0] + " inputfile outputfile")
	exit(0)
iFile = sys.argv[1]
oFile = sys.argv[2]

# Detect codecs in input file
BOM = b'\xef\xbb\xbf'
existBom = lambda s: True if s==BOM else False
#with open(iFile, "rb") as iFile:
f = open(iFile, "rb")
CODEC = "utf-8-sig" if existBom(f.read(3)) else "utf-8"
f.close()

# Load source file
with open(iFile, "r", encoding=CODEC) as iFile:
	inStr = iFile.read()

tags = eval(inStr)[0]["Tags"]
outDict = eval(MAINBODY)
tasks = []

for tag in tags:
	if ".linkedin." in tag["Url"]:
		task = eval(LINKEDIN)
	elif "www.indeed." in tag["Url"]:
		task = eval(WWWINDEED)
	elif "cn.indeed." in tag["Url"]:
		task = eval(CNINDEED)
	elif "jp.indeed." in tag["Url"]:
        task = eval(JPINDEED)
    elif ".zhaopin." in tag["Url"]:
        task = eval(ZHAOPIN)
    elif ".nasdaq." in tag["Url"]:
        task = eval(NASDAQ)
    elif "ru.indeed." in tag["Url"]:
		task = eval(RUINDEED)
	else:
		raise Exception("UNKNOW WEB SITE: " + tag["Url"])

	task["Name"] = tag["Name"]
	task["Url"] = tag["Url"]
	tasks.append(task)

outDict["Tasks"] = tasks

with open(oFile, 'w') as oFile:
	json.dump(outDict, oFile, indent=4)

