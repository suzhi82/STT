16:00 2018-07-01

ʵ��������ͬ��Python ������WebDriver���������ttt.py ��stt.py û��̫�ൽ����
������Ҫ��Linux ��Windows ֮ǰά����ʵ�ַ��ϲ���ϵͳƽ̨���Եĸ��Ի��������Էֿ�������ͬ����������


13:03 2017-10-29

���ߣ�������.D.��

��Ŀ��Ҫ�ļ�

����ƽ̨��
http://releases.ubuntu.com/trusty/ubuntu-14.04.5-desktop-amd64.iso

ע��������Ҫ��װ��VMWare Tools�����ڡ���������˵��£��ο���
https://jingyan.baidu.com/article/fc07f98977b60f12ffe5199b.html

�ֱ�������(������Ubuntu ������ʾ��С)
������Ļ���Ͻ�ʱ���ұߵĳ���ͼ��
-->System Setting -->Displays -->Resolution��������1280*800�����Apply(���½��ܿ��������ť) ���ɡ�

����SSH ����
sudo apt-get update
sudo apt-get install openssh-server -y

ƽ̨����汾
chromedriver_linux64.zip
firefox-56.0.2.tar.bz2
geckodriver-v0.19.0-linux64.tar.gz
google-chrome-stable_current_amd64.deb Version 62.0.3202.75 (Official Build) (64-bit)
linux-image-4.13.9-041309-generic_4.13.9-041309.201710211231_amd64.deb
phantomjs-2.1.1-linux-x86_64.tar.bz2
Python-3.6.3.tar.xz
selenium-3.6.0.tar.gz


-------------------------------------------------------------------

�����ļ�

stt.py    �������(��������������κ�.py �ļ���log �ļ�������־�ļ�����֮�ı�)

������
1��ʹ��Ĭ�������ļ� (Ĭ��ʹ�õ�ǰĿ¼�µ�stt.conf �����ļ�������ļ�������result �ļ���)
python3 stt.py

2��ָ�������ļ� (ʹ�õ�ǰĿ¼�µ�bbb1.conf �����ļ�������ļ�������result �ļ���)
python3 stt.py -c bbb1.conf

3��ָ�������ļ��ͽ���ļ� (ʹ�õ�ǰĿ¼�µ�bbb1.conf �����ļ�������ļ�Ϊ��ǰĿ¼�µ�111.csv)
python3 stt.py -c bbb1.conf -o 111.csv

4���鿴����
python3 stt.py -h


-------------------------------------------------------------------

ttt.conf  Ĭ�������ļ�(���������Ϊstt.py ʱ)

�ؼ�������飺
"Initialization":		# ��ʼ������
    "MaxThreads": 5		# ����߳�����1GB �ڴ���಻Ҫ����5 ���߳�
    "SearchTimeout": 60		# ������ҳԪ�س�ʱʱ�䣬Ĭ������5 ����ÿ�������ִ��ʱ��
    "Browser": "PhantomJS"	# ����ҳ����Ⱦ���������֧��Firefox��Chrome ���޽����PhantomJS����Ҫ���ⰲװWebDriver����������а汾Ҫ��
    "CSVTitle": "ICT"		# ����ļ����ݵı��⣬��ʾ������CSV 

"Tasks"				# ÿ��task ��Ӧһ���ɼ����������������ŵ�һ��Queue �У�����̴߳Ӷ�������ȡ����ֱ������Ϊ��
				# ����ÿ����վ�����Ի��в�ͬ��������������磺��Ҫ��¼��Login����Ҫ���˽����Filter �ȵ�


����������⣬�������£�
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

��������Tasks ��[] ��������������ÿ����һ��{} ����һ����������֮���ö��Ÿ�����
�����������
Name		# �������ƣ������ظ�����Ӱ������CSV �ļ��ֶ�����
Url		# ����������վ�����ӣ�ȷ����������Ч��
Locating	# ��ҳ�ϵ�Ԫ�ض�λ��֧�ֶ��ַ�ʽ��xpath��css selector��id �ȡ�
Login		# ��վ�Ƿ���Ҫ��¼��������¼�Ĳ������粻��Ҫ��д�����ԡ�
Filter		# ��������Ƿ���Ҫ���ˣ��粻��Ҫ��д�����ԡ�


-------------------------------------------------------------------

mgf.sh  �������csv �ļ��ϲ��ű�

������
mgf.sh results/T

�Ὣresults/T*.csv �ļ����ϲ�����ǰ8 Ϊ��������ļ�����csv �ļ��С�


-------------------------------------------------------------------

det.py    ������Գ���

������
python3 det.py -m test/test.task -b Firefox -t 15

������
-m  ��ѡ�������ļ�
-b  ��ѡ���������Ĭ��PhantomJS
-t  ��ѡ����ʱ���ã�15 �룬���������������������3 ��

�����ļ���ʽtest.task
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

htc.py    ����ת��(����version_0.2.1 ICT ��Ar.exe ��conf.json)

������
����ָ�� Դ�ļ� Ŀ���ļ�
python3 htc.py conf.org.json aaa1.conf

�����Ŀ¼��
python3 htc.py test/conf.org.json test/aaa2.conf


-------------------------------------------------------------------

��Դ���ο���վ

��ƽ̨�ű�����Python3
https://www.python.org/

�Զ������Կ��Selenium
http://www.seleniumhq.org/

�޽��������PhantomJS
http://phantomjs.org/

���������֧��Selenium ��WebDriver
http://selenium-python.readthedocs.io/installation.html#drivers

���漰������汾��ο�QQ �ʼ��ʼ�
��Ubuntu-14.04.5 ����Selenium ���������°�


-------------------------------------------------------------------

