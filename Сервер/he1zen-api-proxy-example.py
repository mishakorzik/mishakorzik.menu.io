import requests, json

start = True

    while start:

        try:

            url = "{{settings.apiurl}}/api/proxy/socks5"

            get = requests.get(url).json()

            ip = get["address"]

            port = get["port"]

            proxies = {"http": f"socks5://{ip}:"+str(port)}

            myip = requests.get("https://api.ipify.org", timeout=3, proxies=proxies).text

            print(myip)

            start = False

        except:

            print("proxy not work, finding new proxy.")
