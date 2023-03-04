import requests
print("found 3 working proxy servers")
for i in range(3):
   get = requests.get("http://127.0.0.1:8080/api/proxy/socks5").json()
   ip = str(get["address"])
   port = str(get["port"])
   country = str(get["country"])
   print(f"{ip}:{port} - {country}")
