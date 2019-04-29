16:00 2018-07-01

实际上在相同到Python 环境、WebDriver和浏览器下ttt.py 和stt.py 没有太多到区别，
由于需要在Linux 和Windows 之前维护，实现符合操作系统平台特性的个性化设置所以分开两个不同命名到程序。


13:03 2017-10-29

作者：五月书.D.店

项目主要文件

部署平台：
http://releases.ubuntu.com/trusty/ubuntu-14.04.5-desktop-amd64.iso

注意的是最后要安装“VMWare Tools”，在“虚拟机”菜单下，参考：
https://jingyan.baidu.com/article/fc07f98977b60f12ffe5199b.html

分辨率设置(不设置Ubuntu 界面显示很小)
单击屏幕右上角时间右边的齿轮图标
-->System Setting -->Displays -->Resolution，调整到1280*800，点击Apply(右下角能看到半个按钮) 即可。

开启SSH 服务
sudo apt-get update
sudo apt-get install openssh-server -y

平台软件版本
chromedriver_linux64.zip
firefox-56.0.2.tar.bz2
geckodriver-v0.19.0-linux64.tar.gz
google-chrome-stable_current_amd64.deb Version 62.0.3202.75 (Official Build) (64-bit)
linux-image-4.13.9-041309-generic_4.13.9-041309.201710211231_amd64.deb
phantomjs-2.1.1-linux-x86_64.tar.bz2
Python-3.6.3.tar.xz
selenium-3.6.0.tar.gz


-------------------------------------------------------------------

程序文件

stt.py    爬虫程序(可以随便命名成任何.py 文件，log 文件夹下日志文件名随之改变)

用例：
1、使用默认配置文件 (默认使用当前目录下的stt.conf 配置文件，结果文件生成在result 文件夹)
python3 stt.py

2、指定配置文件 (使用当前目录下的bbb1.conf 配置文件，结果文件生成在result 文件夹)
python3 stt.py -c bbb1.conf

3、指定配置文件和结果文件 (使用当前目录下的bbb1.conf 配置文件，结果文件为当前目录下的111.csv)
python3 stt.py -c bbb1.conf -o 111.csv

4、查看帮助
python3 stt.py -h


-------------------------------------------------------------------

ttt.conf  默认配置文件(爬虫程序名为stt.py 时)

关键参数简介：
"Initialization":		# 初始化参数
    "MaxThreads": 5		# 最大线程数，1GB 内存最多不要超过5 个线程
    "SearchTimeout": 60		# 查找网页元素超时时间，默认它的5 倍是每个任务的执行时限
    "Browser": "PhantomJS"	# 用于页面渲染的浏览器，支持Firefox、Chrome 及无界面的PhantomJS，需要另外安装WebDriver，对浏览器有版本要求
    "CSVTitle": "ICT"		# 结果文件内容的标题，显示在最终CSV 

"Tasks"				# 每个task 对应一个采集工作，所有任务会放到一个Queue 中，多个线程从队列中领取任务直至队列为空
				# 根据每个网站的特性会有不同的任务参数，例如：需要登录的Login，需要过滤结果的Filter 等等


任务配置详解，样例如下：
    "Tasks": [
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
        },
        {
            "Name": "cloud US indeed",
            "Url": "http://www.indeed.com/q-cloud-l-United-States-jobs.html",
            "Locating": {
                "ByType": "xpath",
                "Location": "//*[@id=\"searchCount\"]"
            },
            "Filter": "%s.split('of')[-1]"
        }
    ]

整个任务集Tasks 由[] 包含起来，里面每个第一层{} 代表一个任务，它们之间用逗号隔开。
任务基本属性
Name		# 任务名称，不可重复，会影响最终CSV 文件字段名。
Url		# 被搜索的网站的链接，确保该链接有效。
Locating	# 网页上的元素定位，支持多种方式：xpath，css selector，id 等。
Login		# 网站是否需要登录，包含登录的参数，如不需要则不写该属性。
Filter		# 搜索结果是否需要过滤，如不需要则不写该属性。


-------------------------------------------------------------------

mgf.sh  新增结果csv 文件合并脚本

用例：
mgf.sh results/T

会将results/T*.csv 文件都合并到当前8 为日期组成文件名的csv 文件中。


-------------------------------------------------------------------

det.py    任务调试程序

用例：
python3 det.py -m test/test.task -b Firefox -t 15

参数：
-m  必选，任务文件
-b  可选，浏览器，默认PhantomJS
-t  可选，超时设置，15 秒，浏览器整个生命周期是其3 倍

任务文件格式test.task
{
    "Name": "TSLA LINKEDIN CAREER",
    "Url": "https://www.linkedin.com/jobs/search/?keywords=tesla&location=Worldwide",
    "Locating": {
        "ByType": "css selector",
        "Location": "div.jobs-search-results__count-string"
    },
    "Login": {
        "LoginUrl": "https://www.linkedin.com/",
        "Username": {
            "ByType": "id",
            "Location": "login-email",
            "Input": "ren.li.vic@gmail.com"
        },
        "Password": {
            "ByType": "id",
            "Location": "login-password",
            "Input": "Spike777"
        },
        "LogonFlag": {
            "ByType": "id",
            "Location": "jobs-nav-item"
        }
    }
}


-------------------------------------------------------------------

htc.py    配置转换(适配version_0.2.1 ICT 里Ar.exe 的conf.json)

用例：
必须指定 源文件 目标文件
python3 htc.py conf.org.json aaa1.conf

或带上目录的
python3 htc.py test/conf.org.json test/aaa2.conf


-------------------------------------------------------------------

资源及参考网站

跨平台脚本语言Python3
https://www.python.org/

自动化测试框架Selenium
http://www.seleniumhq.org/

无界面浏览器PhantomJS
http://phantomjs.org/

各种浏览器支持Selenium 的WebDriver
http://selenium-python.readthedocs.io/installation.html#drivers

所涉及的软件版本请参看QQ 邮件笔记
《Ubuntu-14.04.5 配置Selenium 环境》最新版


-------------------------------------------------------------------

