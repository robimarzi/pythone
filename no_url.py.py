import urllib.request
from bs4 import BeautifulSoup
import requests
import pandas as pd

link =  "https://www.amazon.it/"
risposta = urllib.request.urlopen(link)                         
html = risposta.read().decode()                                 
prova = BeautifulSoup(html, "html.parser")                      
all_links = [a["href"] for a in prova.find_all("a", href=True)] 

df = pd.DataFrame(columns=["Link"])
lista = []
for valididamento in all_links:                                 
   if valididamento.startswith("http"):
        a = urllib.request.urljoin(link, valididamento)         
        try: 
            a = requests.get(a)
            if not a.status_code == 200:                       
                lista.append(valididamento)
        except:
                pass
for i in lista:
    df.loc[len(df)] = i                                         
print(df.head(10))
   
