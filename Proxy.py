import threading
import requests

global info
global proxy

def generateproxy():
				global proxy
				global info

				print(Fore.YELLOW+"Genering Proxy Please wait be patient ..."+Style.RESET_ALL)
				url="https://raw.githubusercontent.com/mishakorzik/mishakorzik.menu.io/master/%D0%A1%D0%B5%D1%80%D0%B2%D0%B5%D1%80/ProxyList.txtU"
				req = requests.get(url)
				ip = requests.get("https://raw.githubusercontent.com/mishakorzik/mishakorzik.menu.io/master/docs/ip").text
				array = req.text.split()
				open("proxies.txt", "w+").close()
				for prox in array:
					      thread_list = []
					      t = threading.Thread (target=checkproxy, args=(ip, prox))
					      thread_list.append(t)
					      t.start()
				time.sleep(1)
				f = open("proxies.txt")
				proxies = f.read().split()
				proxy = random.choice(proxies)
				info = Fore.GREEN+"Working proxy successfully found!"+Style.RESET_ALL

def checkproxy(ip, prox):
				try:
                ipx = requests.get("https://raw.githubusercontent.com/mishakorzik/mishakorzik.menu.io/master/docs/ip", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}, verify=False, timeout=10).text
				except:
					      ipx = ip
				if ip != ipx:
					      f = open("proxies.txt", "a+")
					      f.write("{}\n".format(prox))
                f.close()
					f.close()
