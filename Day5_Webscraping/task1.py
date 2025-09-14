#14/09/2025

import requests
from bs4 import BeautifulSoup

def scrape(): 
    #the target url we are scraping from
    url = 'https://www.geeksforgeeks.org/python/python-programming-language-tutorial/'
    response = requests.get(url) #Make a request instances 
    print(response.text[:100]) #show the first 500 characters
    #using BeautifulSoup 
    soup = BeautifulSoup(response.text, 'html.parser')

    #Displaying elements of page 
    print("Title of page is: \t")
    for title in soup.find_all('h1'):
        print(title.get_text()) 
    for subheadings in soup.find_all('h2'):
        print(subheadings.get_text())
    for links in soup.find_all('a'):
        print(links.get_text())


if __name__ == '__main__':
    scrape()

