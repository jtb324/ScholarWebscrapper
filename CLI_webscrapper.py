from bs4 import BeautifulSoup
import requests


def getSoup(address):
    page = requests.get(address)
    soup = BeautifulSoup(page.content, "html.parser")
    print(page.status_code)
    print(soup)
