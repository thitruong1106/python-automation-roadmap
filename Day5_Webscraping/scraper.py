"""
    Scrape products name and price from books to scrape. 
"""

import requests
from bs4 import BeautifulSoup
import csv
def scrape():
    url = 'https://books.toscrape.com/' 
    req = requests.get(url) # Make a request instance 
    soup = BeautifulSoup(req.text, 'html.parser')

    #Find all books
    #Each product is encapsulted in an article.product_pod
    books = soup.find_all("article", class_ = "product_pod")
    #For each book 
    for book in books:
        #get the name of book. h3>a>title
        title = book.h3.a["title"] 
        #Get the price 
        #p class="price_colour"
        price = book.find("p", class_="price_color").text.strip() #Print in terminal

        print(f"{title} - {price}")
        with open("books.csv", "w", newline = "", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Book Title", "Price"])
            for book in books:
                title = book.h3.a["title"] 
                price = book.find("p", class_="price_color").text.strip()
                writer.writerow([title,price]) #For each row, log a book and its price
if __name__ == '__main__': 
    scrape()
    