#!/usr/bin/env python3
# -*-coding:utf-8 -*-

__author__ = 'yoshubom'
__version__ = '1.0'

import os, sys, getopt, json, threading, queue, re, timeit, time, logging, traceback, csv
from selenium import webdriver
from logging.handlers import RotatingFileHandler
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Method for console and file logger
def getCnFLogger(logfile):
	# Step1. Create a logger  
	logger = logging.getLogger()
	logger.setLevel(logging.INFO)    # Log global level  

	# Step2. Create a handler for rotating log file (5MB each, 5 files, oldest data will be overrided)
	rh = RotatingFileHandler(logfile, mode='a', maxBytes=5*1024*1024, backupCount=3)
	#fh.setLevel(logging.DEBUG)   # Output to file's log level  

	# Step3. Create a handler for output to console
	ch = logging.StreamHandler()
	#ch.setLevel(logging.WARNING)   # console's log level

	# Step4. Define log format and set it to all log handlers  
	formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
	rh.setFormatter(formatter)
	ch.setFormatter(formatter)

	# Step5. add all handlers to logger
	logger.addHandler(rh)
	logger.addHandler(ch)

	return logger


# Class for task thread
class TaskThread(threading.Thread):

	# Static variables for share resource visited saftly by multi-threads
	threadLock = threading.Lock()
	taskResults = {}

	# Static Method for setting task queue and results
	def setTaskQueue(tasks):
		TaskThread.taskQueue = queue.Queue(len(tasks))
		#[TaskThread.taskQueue.put(task) for task in tasks]
		for task in tasks:
			TaskThread.taskResults[task["Name"]] = 0
			TaskThread.taskQueue.put(task)

	def __init__(self, tid):
		threading.Thread.__init__(self)
		self.threadId = str(tid)

	# Override threading.Thread.run()
	def run(self):
		LOGGER.info("Thread " + self.threadId + " started!!!")
		self.__huntElement(TaskThread.taskQueue, TaskThread.threadLock, TaskThread.taskResults)
		LOGGER.info("Thread " + self.threadId + " finished!!!")

	# Method for handling task
	def __huntElement(self, taskQueue, threadLock, taskResults):
		while True:
			try:
				# If there is no task throws queue.Empty exception
				threadLock.acquire()
				if taskQueue.empty():
					task = None
					threadLock.release()
					break

				# Get task from queue
				task = taskQueue.get(True)
				threadLock.release()

				LOGGER.info("Task started: " + task["Name"] + " in Thread(" + self.threadId + ")")

				# Dynamically get browser by eval()
				if "FirefoxHeadless" == BROWSER:
					fireFoxOptions = webdriver.FirefoxOptions()
					fireFoxOptions.set_headless()
					browser = webdriver.Firefox(firefox_options=fireFoxOptions)
				elif "ChromeHeadless" == BROWSER:
					chromeOptions = webdriver.ChromeOptions()
					chromeOptions.set_headless()
					browser = webdriver.Chrome(chrome_options=chromeOptions)
				else:
					browser = eval('webdriver.' + BROWSER + '()')

				# Implicit wait for the lifetime of the browser
				#browser.implicitly_wait(THREAD_TIMEOUT)   # implicity_wait will increase WebDriverWait waiting time
				# Timeout of the browser.get() method
				browser.set_page_load_timeout(SEARCH_TIMEOUT*2)
				# Explicit wait object
				wait = WebDriverWait(browser, SEARCH_TIMEOUT)

				# If web login required
				if "Login" in task:
					lparams = task["Login"]
					try:
						LOGGER.info("Task visiting LoginUrl: " + task["Name"] + " in Thread(" + self.threadId + ")")
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
						LOGGER.info("Task logging in: " + task["Name"] + " in Thread(" + self.threadId + ")")
						element = wait.until(EC.presence_of_element_located((lparam["ByType"], lparam["Location"])))
						LOGGER.info("Task logged in: " + task["Name"] + " in Thread(" + self.threadId + ")")

				lparam = task["Locating"]
				try:
					LOGGER.info("Task page loading: " + task["Name"] + " in Thread(" + self.threadId + ")")
					browser.get(task["Url"])
				except TimeoutException as te: LOGGER.info("Task page loading timeout: " + task["Name"] + " in Thread(" + self.threadId + ")")
				except: raise
				finally:
					# Even if the page loading timeout error occur, needing to check whether the data is on the page.
					LOGGER.info("Task page searching: " + task["Name"] + " in Thread(" + self.threadId + ")")

					# str.strip() return a copy of string to result, just in case element object is invalid after browser.quit().
					result = wait.until(EC.visibility_of_element_located((lparam["ByType"], lparam["Location"]))).text.strip()
					browser.quit()

					LOGGER.info(result + " in Thread(" + self.threadId + ")")
					# Dynamically invoke filter method by eval()
					if "Filter" in task:
						fstr = task["Filter"] % 'result'
						LOGGER.info(fstr + " in Thread(" + self.threadId + ")")
						result = eval(fstr)

					# Remove per mill sign
					result = result.replace(",", "")
					# Remove all non-numeric characters from result
					#result = re.sub("\D", "", result)

					# Extract the number from the result by Regular Expression
					result = re.findall(r"\d+\.?\d*", result)[0]

					# [on_true] if [expression] else [on_false]
					result = 0 if result.strip() == '' else result

					# Offer main thread to refine the result
					threadLock.acquire()
					taskResults[task["Name"]] = result
					threadLock.release()

					LOGGER.info(str(result) + " in Thread(" + self.threadId + ")")
					LOGGER.info("Task finished: " + task["Name"] + " in Thread(" + self.threadId + ")")

			except Exception as e:
				if task != None:
					LOGGER.error("In task: \'" + task["Name"] + "\' in Thread(" + self.threadId + ") " + ''.join(traceback.format_exception(*sys.exc_info())))

			finally:
				browser.quit()



# Main thread
if __name__ != "__main__": exit(0)
try:
	# Check Python version
	if sys.version_info < (3, 6, 2): raise RuntimeError('At least Python 3.6.2 is required')

	# Record start time
	t_start = timeit.default_timer()

	# Initialization
	# All files have the same name as program by default
	DATETIME = time.strftime('%Y-%m-%d_%H%M%S',time.localtime(time.time()))
	PROGRAM_NAME = os.path.basename(__file__).split('.')[0]
	CONFIG_FILE = PROGRAM_NAME + ".conf"
	CURRENT_DIR = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
	RESULTS_DIR = CURRENT_DIR + "/results/"
	os.mkdir(RESULTS_DIR) if not os.path.exists(RESULTS_DIR) else print(RESULTS_DIR)
	LOG_DIR = CURRENT_DIR + "/log/"
	os.mkdir(LOG_DIR) if not os.path.exists(LOG_DIR) else print(LOG_DIR)
	OUTPUT_FILE = RESULTS_DIR + DATETIME + ".csv"
	LOG_FILE = LOG_DIR + PROGRAM_NAME + ".log"
	USAGE_STR = 'Uage: python3 ' + sys.argv[0] + ' [-c <configfile>] [-o <outputfile>] [-h]'

	# Get srguments from command line including configure file and logging file
	opts, args = getopt.getopt(sys.argv[1:], "hc:o:", ["configfile=", "outputfile="])
	for opt, arg in opts:
		if opt == '-h':
			print(USAGE_STR)
			sys.exit(0)
		elif opt in ("-c", "--configfile"):
			CONFIG_FILE = arg
		elif opt in ("-o", "--outputfile"):
			OUTPUT_FILE = arg

	# Get logger object
	LOGGER = getCnFLogger(LOG_FILE)

	# Read configure file. Keyword 'with' will close file automatically.
	with open(CONFIG_FILE, 'r', encoding='utf-8') as configFile:
		jsonConfig = json.load(configFile)

	# Global Constants
	initParams = jsonConfig["Initialization"]
	SEARCH_TIMEOUT = initParams["SearchTimeout"]
	THREAD_TIMEOUT = SEARCH_TIMEOUT * 6
	MAX_THREADS = initParams["MaxThreads"]
	BROWSER = initParams["Browser"]
	CSV_TITLE = initParams["CSVTitle"]
	# Set default browser
	if BROWSER not in ["Chrome", "ChromeHeadless", "Firefox", "FirefoxHeadless"]:
		BROWSER = "FirefoxHeadless"

	# Create tasks queue
	TaskThread.setTaskQueue(jsonConfig["Tasks"])
	threads = []
	queueSize = TaskThread.taskQueue.qsize()
	for tid in range(MAX_THREADS if MAX_THREADS < queueSize else queueSize):
		#thread = threading.Thread(target=huntElement,args=(task,))
		thread = TaskThread(tid)
		threads.append(thread)
		thread.setDaemon(True)
		thread.start()

	# Main thread wait for each sub-thread finish
	while not TaskThread.taskQueue.empty(): time.sleep(1)
	for thread in threads:
		thread.join(THREAD_TIMEOUT+10)

	# Put results into outputfile
	with open(OUTPUT_FILE, 'w', newline='') as outPutFile:
		outPutWriter = csv.writer(outPutFile)
		outPutWriter.writerow([CSV_TITLE])
		outPutWriter.writerow(TaskThread.taskResults.keys())
		outPutWriter.writerow(TaskThread.taskResults.values())


	LOGGER.info("Saved to " + OUTPUT_FILE)


except getopt.GetoptError:
	print(USAGE_STR)
	sys.exit(1)

except Exception as e:
	LOGGER.error(''.join(traceback.format_exception(*sys.exc_info())))
	raise e

finally:
	# Record end time and calculate consuming time
	t_end = timeit.default_timer()
	if 'LOGGER' in dir():
		LOGGER.info("All " + str(queueSize) + " tasks done! Consuming time(s): " + str(t_end-t_start))

		# Clean all the browser processes
		cmdStrs = []
		if "Chrome" in BROWSER:
			cmdStrs.append("taskkill /F /T /IM chrome.exe")
			cmdStrs.append("taskkill /F /T /IM chromedriver.exe")
		elif "Firefox" in BROWSER:
			cmdStrs.append("taskkill /F /T /IM firefox.exe")
			cmdStrs.append("taskkill /F /T /IM geckodriver.exe")
		else:
			pass

		for cmdStr in cmdStrs:
			LOGGER.info(cmdStr)
			os.system(cmdStr)
			
		LOGGER.info("===================================================================")


