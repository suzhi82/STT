# Search Target Tool

## Requirements
Python3 >= 3.6  
Selenium >= 3.13.0  
Chrome >= 66.0  
Firefox >= 61.0  
chromedriver:	https://sites.google.com/a/chromium.org/chromedriver/downloads  
geckodriver:	https://github.com/mozilla/geckodriver/releases  


## Usage
python3 ttt.py [-c <configfile>] [-o <outputfile>] [-h]
### Example
/usr/bin/python3.6 /home/STT/stt.py -c /home/STT/A01-ICT.conf -o /home/STT/results/A01-ICT.csv


## Configuration(JSON Format)
<pre name="code" class="json">
Comment  
Name  
Initialization  
    Comment  
        MaxThreads  
        SearchTimeout  
        Browser ChromeHeadless  
        CSVTitle  
Tasks  
    Name  
    Url  
    Login  
        LoginUrl  
            Username  
                ByType  
                Location  
                Input  
            Password  
                ByType  
                Location  
                Input  
            LogonFlag  
                ByType  
                Location  
    Locating  
        ByType  
        Location  
</pre>
  

## Update Logs
#### 2019-03-20 21:31:47
默认浏览器设置为ChromeHeadless，因FirefoxHeadless 跟驱动经常connection refused。
全局的变量大写，在局部引用时加关键字global。
关闭browser 对象之前先检查是否存在该变量且不为None。
bms.sh 全部设置为sleep 10，十秒足够了。sleep 并不是ttt.py 执行所需的时间。

#### 2019-03-19 09:17:07
程序一开始将配置文件名和结果文件名打印到屏幕及日志文件里。

#### 2019-03-11 21:08:16
每启动一个task 的时候在Using 浏览器后面显示taskSeq/task 总数。

#### 2019-03-05 19:35:12
当配置文件出现不知名浏览器默认用FirefoxHeadless。
更新了Chrome 和Firefox 用headless 模式的代码，之前已经被官方摒弃。
修正了重复quit 浏览器导致出现的多余日志错误，加入了退出浏览器前的判断。

#### 22:26 2018-08-12
主程序没有修改，lnkd.conf 配置文件修改了。
因为LinkedIn 在登录之后要求添加手机号，所以登录成功的Flag 改为Phone-number，
但是页面上点击一次Skip 之后又不用添加手机号了，所以原来的判断标识。
搜索结果页面的css selector 改变了，换了新的又有结果了。
主要就是以上两点改变。

#### 23:36 2018-06-30
新版Selenium 不再支持PhantomJS，同时Firefox 56 之后开始支持Headless 模式，
所以将ttt.py 主程序更新为支持Firefox 和Chrome 到无界面模式，方便结合GUI 调试自动化脚本。
LinkedIn 某些页面不再支持PhantomJS，所以必须改成ChromeHeadless 或FirefoxHeadless，详见配置文件lnkd.conf。

注意：Chrome >= 66.0，Firefox >=61.0，Python >= 3.6.2 
具体案子步骤详见《Ubuntu-14.04.5 配置Selenium 环境》
chromedriver_linux64.zip
geckodriver-v0.21.0-linux64.tar.gz
google-chrome-stable_current_amd64.deb
selenium-3.13.0.tar.gz

#### 16:00 2018-07-01
实际上在相同到Python 环境、WebDriver和浏览器下ttt.py 和stt.py 没有太多到区别，
由于需要在Linux 和Windows 之前维护，实现符合操作系统平台特性的个性化设置所以分开两个不同命名到程序。

