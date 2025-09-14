from bs4 import BeautifulSoup
import requests

def scrape(): 
    url = 'https://remoteok.com/' 
    reqs = requests.get(url)#Request from url 
    soup = BeautifulSoup(reqs.text, 'html.parser')

    print("Title of page is: \t")
    for title in soup.find_all('h1'):
        print(title.get_text())

if __name__ == '__main__':
    scrape()

#Work in progress for day 6