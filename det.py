#!/usr/bin/env python3.6
# -*-coding:utf-8 -*-

__author__ = 'yoshubom'

import re, sys, getopt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



# Method for handling task
def huntElement(task):
	try:
		# Dynamically get browser by eval()
		browser = eval('webdriver.' + BROWSER + '()')
		# Implicit wait for the lifetime of the browser
		browser.implicitly_wait(THREAD_TIMEOUT)
		# Timeout of the browser.get() method
		browser.set_page_load_timeout(SEARCH_TIMEOUT)
		# Explicit wait object
		wait = WebDriverWait(browser, SEARCH_TIMEOUT)

		# If web login required
		if "Login" in task:
			lparams = task["Login"]
			try:
				print("Task visiting LoginUrl: " + task["Name"])
				browser.get(lparams["LoginUrl"])
			except TimeoutException as te: pass
			except: raise
			finally:
				lparam = lparams["Username"]
				element = wait.until(EC.visibility_of_element_located((lparam["ByType"], lparam["Location"])))
				element.send_keys(lparam["Input"])
				lparam = lparams["Password"]
				element = wait.until(EC.visibility_of_element_located((lparam["ByType"], lparam["Location"])))
				element.send_keys(lparam["Input"])
				element.send_keys(Keys.RETURN)
				#browser.find_element_by_id("login-submit").click()
				lparam = lparams["LogonFlag"]
				# Wait until login is successful
				print("Task logging in: " + task["Name"])
				element = wait.until(EC.presence_of_element_located((lparam["ByType"], lparam["Location"])))
				print("Task logged in: " + task["Name"])

		lparam = task["Locating"]
		try:
			print("Task page loading: " + task["Name"])
			browser.get(task["Url"])
		except TimeoutException as te: print("Task page loading timeout: " + task["Name"])
		except: raise
		finally:
			# Even if the page loading timeout error occur, needing to check whether the data is on the page.

			# str.strip() return a copy of string to result, just in case element object is invalid after browser.quit().
			result = wait.until(EC.visibility_of_element_located((lparam["ByType"], lparam["Location"]))).text.strip()
			#browser.quit()

			print(result)
			# Dynamically invoke filter method by eval()
			if "Filter" in task:
				fstr = task["Filter"] % 'result'
				print(fstr)
				result = eval(fstr)

			# Remove per mill sign
			result = result.replace(",", "")
			# Remove all non-numeric characters from result
			#result = re.sub("\D", "", result)

			# Extract the number from the result by Regular Expression
			result = re.findall(r"\d+\.?\d*", result)[0]

			# [on_true] if [expression] else [on_false]
			result = 0 if result.strip() == '' else result


			print(str(result))
			print("Task finished: " + task["Name"])

	except: raise
	finally:
		if "PhantomJS" == BROWSER: browser.quit()



# Main thread
if __name__ == "__main__":

	# Initialization
	USAGE_STR = 'Uage: python3 ' + sys.argv[0] + ' -m <missionfile> [-b <browser>] [-t <timeout>] [-h]'
	SEARCH_TIMEOUT = 30
	BROWSER = "PhantomJS"
	MISSION_FILE = ""

	# Get srguments from command line
	opts, args = getopt.getopt(sys.argv[1:], "hm:b:t:", ["mission=", "browser=", "timeout=", "help"])
	for opt, arg in opts:
		if opt in ("-m", "--missionfile"):
			MISSION_FILE = arg
		elif opt in ("-b", "--browser"):
			BROWSER = arg
		elif opt in ("-t", "--timeout"):
			SEARCH_TIMEOUT = arg
		
	if len(sys.argv) < 1 or MISSION_FILE == "":
		print(USAGE_STR)
		sys.exit(0)

	THREAD_TIMEOUT = SEARCH_TIMEOUT * 3
	
	# Load mission file
	with open(MISSION_FILE, "r") as msnFile:
		mStr = msnFile.read()

	task = eval(mStr)

	huntElement(task)


