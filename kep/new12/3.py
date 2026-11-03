import requests
import matplotlib.pyplot as plt
from datetime import date, timedelta

r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
cur = r.json()[11]["cc"]

d = date.today()
start = (d - timedelta(days=31)).strftime("%Y%m%d")
end = d.strftime("%Y%m%d")

r = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=" + start + "&end=" + end + "&valcode=" + cur + "&sort=exchangedate&order=desc&json")
data = r.json()

days = [row["exchangedate"] for row in data]
rates = [row["rate"] for row in data]

plt.plot(days, rates, marker="o")
plt.title("Курс " + cur + " до гривні за останній місяць")
plt.xlabel("Дата")
plt.ylabel("UAH")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
