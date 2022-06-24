# Compra de Dollar
import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
dolar = requests.get("https://www.google.com/search?client=opera-gx&q=valor+do+dolar&sourceid=opera&ie=UTF-8&oe=UTF-8").content
soup = BeautifulSoup(dolar, 'dolar.parser')
print(soup.prettify())


#data = datetime.today().strftime('%A-%B-%d-%Y')
#real = float(input("Deseja trocar quantos reais em dollar? "))
#time.sleep(1.5)
#print("Nesta data {},  o dolar se encontra á {} reais".format(data, data))
