import sys
import requests
from bs4 import BeautifulSoup
import csv

page_target = "Tevetron"
page_category = "IC"

componentsDict = {
    "Product Number" : "",
    "Product Package" : "",
    "Product Price" : "",
    "Product Availability" : "",
}

if (page_target == "Tevetron"):
    f = open('tevetron.csv', 'w', encoding='UTF8', newline='')
elif (page_target == "Elmatis"):
    f = open('elmatis.csv', 'w', encoding='UTF8', newline='')
else:
    print("ERROR: Target website is not defined or invalid!")
    sys.exit(1)

writer = csv.writer(f)

if (page_target == "Tevetron"):
    if (page_category == "IC"):
        URL_base = "https://www.tevetron.hr/hr/webshop/ic/16/"
    elif (page_category == "transistors"):
        URL_base = "https://www.tevetron.hr/hr/webshop/tranzistori/68/"
    else:
        print("ERROR: Tevetron doesn't have the requested category!")
        sys.exit(2)
elif (page_target == "Elmatis"):
    if (page_category == "IC"):
        URL_base = "http://www.elmatis.hr/Products.aspx?categoryId=81"
    elif (page_category == "transistors"):
        URL_base = "http://www.elmatis.hr/Products.aspx?categoryId=159"
    else:
        print("ERROR: Elmatis doesn't have the requested category!")
        sys.exit(3)

page = requests.get(URL_base)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("div", class_="product-inner")

if (page_target == "Tevetron"):
    i = 0
    while results:
        for result in results:
            productNumber = result.find("h3").text.strip()
            productPrice = result.find("span", class_ = "cprice1").text.strip()
            productPackage = result.find("h4").text.strip()
            productAvailability = result.find("span", class_="raspolozivost_2 da").text.strip() if result.find("span", class_="raspolozivost_2 da") != None else result.find("span", class_="raspolozivost_2 ne").text.strip()
            writer.writerow([productNumber, productPrice, productPackage, productAvailability])
        i += 1
        if (i%10 == 0):
            print(f"Status: {i}.")
        URL = URL_base + str(i)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("div", class_="product-inner")
elif (page_target == "Elmatis"):
    print("Not implemented")
    sys.exit(4)

f.close()