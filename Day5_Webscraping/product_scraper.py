"""
15/09/2025

Mini Product 2: Product Scraper 

This script scapes products name and prices from webscraper.io test site (laptop section)
The result of this scraper will print the top 5 products and last 3 products with thier prices in the terminal. 
The result of the full product names, and prices will be saved to a csv. 
"""
import requests 
from bs4 import BeautifulSoup
import csv
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
page = requests.get(url)

if page.status_code != 200:
    print("Failed to fetch")
else:
    #else if successful, perform the below 
    print("Successful fetch")
    soup = BeautifulSoup(page.text, 'html.parser')
    #return all items wrapped in this div class
    items = soup.find_all("div", class_="product-wrapper")

    products = []  
    for item in items:
        #Get the name of the item 
        name = item.find("p", class_="description card-text").get_text(strip = True)
        price = item.find("span", attrs={"itemprop": "price"}).get_text(strip = True)
        products.append((name,price))
    TOP_N = 5
    BOTTOM_N = 3
    #Print to terminal for verification 
    print("\n First 5 Products")
    for name, price in products[:TOP_N]:
        print(f"{name}:{price}")
    #print last 3 products
    print("\n Last 3 Products")
    for name,price in products[-BOTTOM_N:]:
        print(f"{name}: {price}")

    with open("products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file) #write to product.csv
        writer.writerow(["Product name", "price"]) #Header row        
        writer.writerows(products)
        
    print(f"\n Saved {len(products)} products have been added to products.csv")