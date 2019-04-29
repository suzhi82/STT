from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--disable-logging')

#chrome_options.binary_location = r'C:\Users\hldh214\AppData\Local\Google\Chrome\Application\chrome.exe'
#chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = '/opt/google/chrome/chrome'

opener = webdriver.Chrome(chrome_options=chrome_options)


opener.get("https://www.baidu.com")

print(opener.title)


