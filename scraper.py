import requests
from bs4 import BeautifulSoup
import csv
import time

f = open('tevetron.csv', 'w', encoding='UTF8', newline='')
writer = csv.writer(f)

componentsDict = {
    "Product Number" : "",
    "Product Package" : "",
    "Product Price" : "",
    "Product Availability" : "",
}

URL_base = "https://www.tevetron.hr/hr/webshop/ic/16/"
page = requests.get(URL_base)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("div", class_="product-inner")
i = 0
while results:
    for result in results:
        productNumber = result.find("h3").text.strip()
        productPrice = result.find("span", class_ = "cprice1").text.strip()
        productPackage = result.find("h4").text.strip()
        productAvailability = result.find("span", class_="raspolozivost_2 da").text.strip() if result.find("span", class_="raspolozivost_2 da") != None else result.find("span", class_="raspolozivost_2 ne").text.strip()
        writer.writerow([productNumber, productPrice, productPackage, productAvailability])
    i = i + 1
    URL = URL_base + str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div", class_="product-inner")
    time.sleep(1)
f.close()