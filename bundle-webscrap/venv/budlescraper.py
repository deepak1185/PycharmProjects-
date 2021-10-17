
import requests
from bs4 import BeautifulSoup

url = "https://www.humblebundle.com/books/cloud-computing-books"
resp = requests.get(url)
# print(r)
# resp.__dict__
# resp.text
soup = BeautifulSoup(resp.text, 'html.parser')

# Header Tiers
#class="tier-header heading-medium js-tier-header"

#soup.find_all('h2')

soup.select("tier-header heading-medium js-tier-header")

