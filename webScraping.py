import requests
from bs4 import BeautifulSoup
import pyautogui as pya

r = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(r.text, 'html.parser')

links = soup.find_all("a")


print(links)