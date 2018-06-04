import urllib
from bs4 import BeautifulSoup as bs

url = "https://myanimelist.net/anime/35849/"
page = urllib.request.urlopen(url)
soup = bs(page, 'html.parser')

score = soup.find('div', attrs={'data-title':'score'}).text.strip()
print(score)
